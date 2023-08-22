import paramiko
import datetime
import logging
import asyncio

from data import api_options, db_options, sftp_options
from telegram_interaction import send_message

# Database connection
from db_connection import engine, Session

# Database models
from models.file_table import FileTable

# Logging configuration
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def list_sftp(hostname: str, port: int, username: str, password: str, directory_path: str):
    """Connect to an SFTP server, read path contents and sent the results to a telegram chat

    Args:
        hostname (str): sftp's hostname (IP Address is preferred)
        port (int): sftp's port
        username (str): your sftp username
        password (str): your sftp password
        directory_path (str): the path you want to watch for new files
    """    
    try:
        transport = paramiko.Transport((hostname, port))
        transport.connect(username=username, password=password)

        sftp = paramiko.SFTPClient.from_transport(transport)
        
        directory_contents = sftp.listdir_attr(directory_path)
        
        listing_message = "Directory Listing:\n"
        
        for item in directory_contents:
            item_path = f"{directory_path}/{item.filename}"
            item_stat = sftp.stat(item_path)
            creation_timestamp = item_stat.st_mtime  # Get the modification timestamp
            
            creation_date = datetime.datetime.fromtimestamp(creation_timestamp).strftime('%Y-%m-%d %H:%M:%S')
            
            listing_message += f"{item.filename} - Creation Date: {creation_date}\n"
        
        sftp.close()
        transport.close()

        send = send_message(listing_message)
        asyncio.run(send)


    except Exception as e:
        # logger.info(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")

def main():
    # populate connection data from imported data.py
    hostname = sftp_options.host
    port = sftp_options.port
    username = sftp_options.user
    password = sftp_options.passwd
    directory_path = "/" # only root

    list_sftp(hostname, port, username, password, directory_path)


if __name__ == "__main__":
    main()

