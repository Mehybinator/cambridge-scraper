<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="favicon.ico" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Cambridge Scraper</h3>

  <p align="center">
    Download And Loop Any English Word In Seconds!
  </p>
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
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

This Project Was Made To Help Ease The Proccess of Downloading Audio For Your English Lessons.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

This Project Uses Requests for HTTP Requests and Beautiful Soup for Scraping html Documents and Pydub for Audio Manipulation with CustomTkinter As Its UI.

* ![Python][Python]
* ![Pydub][Pydub]
* ![CustomTkinter][CustomTkinter]
* ![BeautifulSoup][BeautifulSoup]
* ![requests][Requests]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
### Prerequisites

Pydub Requires ffmpeg Installed, So Make Sure To Install It:
* Windows
  * Scoop
    ```sh
    scoop install ffmpeg
    ```
  * Chocolatey
    ```sh
    choco install ffmpeg
    ```


Create A Python Environment:
  ```sh
  python -m venv env
  ```

Then Activate Your Env using:
* Windows
  ```sh
  .\env\Scripts\activate
  ```

And Install The Requirements:
  ```sh
  pip install -r requirements.txt
  ```

And Run The Script Using:
  ```sh
  python main.py
  ```

Alternatively If The Env Is Not Active:
  ```sh
  env\Scripts\python main.py
  ```

<!-- CONTACT -->
## Contact

Mehran Arkak - mehran.arkak@protonmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[Python]: https://img.shields.io/badge/Python-FFFFFF?logo=python
[Pydub]: https://img.shields.io/badge/Pydub-FFFFFF?logo=python
[CustomTkinter]: https://img.shields.io/badge/CustomTkinter-FFFFFF?logo=python
[BeautifulSoup]: https://img.shields.io/badge/BeautifulSoup-FFFFFF?logo=python
[requests]: https://img.shields.io/badge/requests-FFFFFF?logo=python
[product-screenshot]: screenshot.png
