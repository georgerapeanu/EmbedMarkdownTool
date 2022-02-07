# EmbedMarkdownTool

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** georgerapeanu, EmbedMarkdownTool, twitter_handle, a.rapeanu49@gmail.com, Embed Markdown Tool, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/georgerapeanu/EmbedMarkdownTool">
    <img src="logo.jpg" alt="Project link" width="80" height="80">
  </a>

  <h3 align="center">Embed Markdown Tool</h3>

  <p align="center">
    A tiny app that tries its best to replicate an given image.
    <br />
    <br />
    <a href="https://github.com/georgerapeanu/EmbedMarkdownTool/issues">Report Bug</a>
    ·
    <a href="https://github.com/georgerapeanu/EmbedMarkdownTool/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is just a little python tool that can be used in order to be able to embed files in markdown files.
While the project was designed for markdown only, it may work on any other file type as long as the regex search pattern
from settings.py is changed accordingly. The only known limitation is that you cannot write two 'embed' patterns on the same line.

### Built With

* [Python](https://www.python.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

The only prerequisite is that you must have python installed.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/georgerapeanu/EmbedMarkdownTool.git
   ```

<!-- USAGE EXAMPLES -->
## Usage

To run the app, you simply have to run ```python3 EmbedMarkdownTool.py main_file_path destination_file_path```, 
where `main_file_path` is the path to the main file(the one from which the replacements will start) and `destination_file_path` is the file path to which the result will be stored. The script will, by default, look for `{{%path%}}` strings, and will replace `{{%path%}}` with the content of the file that is at `path`. That file could contain such `{{%path%}}` too, as long as it doesn't cause any circular imports. You can look in the tests folder for some sort of examples: files which contain `valid` in their name are processed by tests and you can look in the `expected` files to see what you would get.


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/georgerapeanu/EmbedMarkdownTool/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. However, currently I would like this project to remain more of a personal one.
However, if you still want to contribute, there might be a chance that your pull request is accepted. In that case, follow the next steps:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/georgerapeanu/EmbedMarkdownTool](https://github.com/georgerapeanu/EmbedMarkdownTool)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/georgerapeanu/EmbedMarkdownTool.svg?style=for-the-badge
[contributors-url]: https://github.com/georgerapeanu/EmbedMarkdownTool/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/georgerapeanu/EmbedMarkdownTool.svg?style=for-the-badge
[forks-url]: https://github.com/georgerapeanu/EmbedMarkdownTool/network/members
[stars-shield]: https://img.shields.io/github/stars/georgerapeanu/EmbedMarkdownTool.svg?style=for-the-badge
[stars-url]: https://github.com/georgerapeanu/EmbedMarkdownTool/stargazers
[issues-shield]: https://img.shields.io/github/issues/georgerapeanu/EmbedMarkdownTool.svg?style=for-the-badge
[issues-url]: https://github.com/georgerapeanu/EmbedMarkdownTool/issues
[license-shield]: https://img.shields.io/github/license/georgerapeanu/EmbedMarkdownTool.svg?style=for-the-badge
[license-url]: https://github.com/georgerapeanu/EmbedMarkdownTool/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/georgerapeanu
