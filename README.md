# Pimeyes.com Scraper
<div align="center">
  <img src="https://img.shields.io/badge/Google_chrome-4285F4?style=for-the-badge&logo=Google-chrome&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"><br>

</div>


## Overview

This tool is a Selenium-based automation script designed to automate the process of uploading a face image to [pimeyes.com](https://pimeyes.com) for reverse face searching. It uploads the image, initiates the search, and then retrieves and outputs the URL of the search results page along with the number of results found.

## Requirements

Before you begin, ensure you have met the following requirements:
- Python 3.11 or higher installed on your machine.
- You have Latest Version of Google Chrome installed.

## Installation & Use
- Clone this repo: ```https://github.com/Nix4444/Pimeyes-scraper```
- Install the requirements: ```pip install -r requirements.txt```
- Add the image to be searched in your working directory.
- Start the bot: ```python main.py```
- Enter the name of the image, and results will be returned.
- You will be limited to 10 searches per IP, so it's better to use proxy or a VPN will work too.
- To use proxies, set ``use_proxy`` in ``main.py`` (Line 8) to ``True`` add them to ``proxies.txt`` in the format: USERNAME:PASS@IP:PORT
- Based on type of proxy, modify the ``line 13`` and change the function to ``fetchsocks5() or fetchhttps() or fetchhttp()``