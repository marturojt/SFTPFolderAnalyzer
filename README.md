<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/marturojt/SFTPValidator">
    <img src="images/logo_sftp.jpeg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SFTP File validator</h3>

  <p align="center">
    A simple script made to validate if a user upload a file in my SFTP server
    <br />
    <br />
    <a href="https://github.com/marturojt/SFTPValidator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/marturojt/SFTPValidator">View Demo</a>
    ·
    <a href="https://github.com/marturojt/SFTPValidator/issues">Report Bug</a>
    ·
    <a href="https://github.com/marturojt/SFTPValidator/issues">Request Feature</a>
  </p>
</div>

<div>
    <ul>
        <li><strong>Python-powered sftp file validator:</strong> This script only need python v3, and simply validate if there is a new file in the server. Once the new file is detected it send a notification using a custom notification service or telegram, mmmm, i will use telegram</li>
    </ul>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

We are bored so, we decided to make this in a more complicated way... Why i waste 5 minutes a day checking if there is a new file, if I can waste 6 hours trying to automate it? Lol


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

[![Python][Python.org]][Python-url]  
[![Love][LoveBadge]][Python-url]

<!-- * [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url] -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get started with your Python Telegram bot project, you will need the following:

- A Telegram account
- A Telegram bot
- Knowledge in Python
- MySQL server (only for have a registry of existing files)

There are a lot of examples and documentation about creating a bot using the bot father ([Botfather](https://t.me/botfather))

Once you have the telegram bot key and your chat or channel id where you want to send the notification, you need to copy tje data.py.dist file and fill the file with your api keys. The connection info for MySQL server need to be in this file too.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/marturojt/SFTPValidator
   ```
2. Install NPM packages
   ```sh
   pip install logging python-telegram-bot sqlalchemy paramiko
   ```
3. Cop `data.py.dist` to `data.py` and enter your api keys and the database credentials
   ```python
    class DBOptions:
    """
    Database connection options class
    """

    def __init__(self, user: str, password: str, host: str, database: str):
        self.user = user
        self.password = password
        self.host = host
        self.database = database


    # Database connection options definitions
    db_options = DBOptions(
                            user='[your username]', 
                            password='[your password]', 
                            host='[your host]', 
                            database='[your database name]'
                            )


    class APIKeys:
        """
        API connection details class
        """

        def __init__(self, telegram_key: str, telegram_chat_id: str):
            self.telegram_key = telegram_key
            self.telegram_chat_id = telegram_chat_id

    # API keys
    api_options = APIKeys(
                            telegram_key='[your key]',
                            telegram_chat_id='[your key]'
                            )

    class SFTPKeys:
        """
        SFTP connection class
        """

        def __init__(self, user: str, passwd: str, host: str, port: int):
            self.user = user
            self.passwd = passwd
            self.host = host
            self.port = port

    # SFTP connection keys
    sftp_options = SFTPKeys(
                            user='[your user]',
                            passwd='[your passwd]',
                            host='[your host]',
                            port='[your port]'
                            )
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Create a basic script
- [x] Connection to database to save history
- [ ] XXX
- [ ] XXX
- [ ] XXX
- [ ] XXX

See the [open issues](https://github.com/marturojt/SFTPValidator/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Arturo Jiménez - [@_systemctl](https://twitter.com/_systemctl) - okami@freejolitos.com

SFTPValidator: [https://github.com/marturojt/SFTPValidator](https://github.com/marturojt/SFTPValidator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/marturojt/SFTPValidator?style=for-the-badge
[contributors-url]: https://github.com/marturojt/SFTPValidator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/marturojt/SFTPValidator?style=for-the-badge
[forks-url]: https://github.com/marturojt/SFTPValidator/network/members
[stars-shield]: https://img.shields.io/github/stars/marturojt/SFTPValidator?style=for-the-badge
[stars-url]: https://github.com/marturojt/SFTPValidator/stargazers
[issues-shield]: https://img.shields.io/github/issues/marturojt/SFTPValidator?style=for-the-badge
[issues-url]: https://github.com/marturojt/SFTPValidator/issues
[license-shield]: https://img.shields.io/github/license/marturojt/SFTPValidator?style=for-the-badge
[license-url]: https://github.com/marturojt/SFTPValidator/blob/dev/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/marturojt
[product-screenshot]: images/ss.jpeg
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[LoveBadge]: https://img.shields.io/static/v1?label=❤️&message=Love&style=for-the-badge&color=red
[Love-url]: https://freejolitos.com
