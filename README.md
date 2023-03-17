
# Web Scraper with Translation to Hindi

 [![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-390/) [![BeautifulSoup Version](https://img.shields.io/badge/beautifulsoup-4.11.2-blue.svg)](https://pypi.org/project/beautifulsoup4/) [![Deep_Translator Version](https://img.shields.io/badge/deep_translator-1.10.1-blue.svg)](https://pypi.org/project/deep-translator/)

This project is a web scraper that translates html files to Hindi. It uses Python, BeautifulSoup, and deep_translator to achieve this goal.

## Table of Contents
- [Getting started](#installation)
	- [Installation](#installation)
-   [Usage](#usage)
-   [Problems Encountered Scraping the Pages](#problems-encountered-scraping-the-pages)
-   [Google Translate](#google-translate)
	- [Limits](#limits)

# # Getting started

## Installation

To install the Python dependencies for this project, run the following command:

`pip install -r requirements.txt` 

To install HTTrack on Ubuntu, run the following command

    $ sudo  apt-get update
    $ sudo  apt-get install httrack webhttrack

## Usage

To use the script, follow these steps:

1.  Run `$ webhttrack -q -%i -w https://www.example.com/ -O "/home/user/websites/example" -n -%P -N0 -s2 -p7 -D -a -K0 -c4 -%k -r2 -G5 -A25000 -F "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" -%F "" +*.png +*.gif +*.jpg +*.jpeg +*.css +*.js -ad.doubleclick.net/* -%s -%u -%B` to start mirroring the webpage and save it on the `/home/user/websites/example` folder.
2.  Run the `main.py` script to translate each HTML file saved from the step above. The scraped pages will be saved to the `/home/user/websites/example` directory, meaning it will rewrite the HTML files, so create a backup if needed.
3.  use serve install it  `$ npm i serve`  and run it `$ serve .` inside the `/home/user/websites/example`  directory to deploy the website locally.

## Scraping the HTML files

The first approach was the first idea that came to my mind, go tag to tag and translate the text inside, sounds pretty straightforward, but it was not that easy as there were tags that had mixed content, meaning its content was text and tags, also when using `<a>` tags inside a `<p>` tag, and so on, so that strategy was a no go, because the mixed tags could not be translated in easy way.

Using BeautifulSoup to load the HTML file and create a node tree like structure of the tags with the `children` attribute it allowed the script to go node to node till it gets to a node that could be translated, then used a recursive function to keep going and translate the entire html file.

Checking if a node is translatable was done by using the NavigableString class of BeautifulSoup, the translation was done immediately and the tag represented by the node had its text updated/replaced by the translated text.


### Problems Encountered scraping the Pages
During the development of this project, I encountered the following problems:

- When mirroring the website and requesting all its subpages it generated a shadown ban on my ip, that caused pages not downloading because all they can render its Cloudflare protection. It can lead to missing files and errors that cannot be detected.

-   Nested and mixed tags with text: In some cases, there were tags nested within other tags, making it difficult to extract the text accurately. To solve this, I used the `children` method in BeautifulSoup to list and separate the tags and the text.
    
-   Wrong tags: Some files had wrong tags, such as opening a `h4` tag and ending with a `h3` tag. This caused issues when translating the text as the translator expected the tags to be well-formed.
    

## Google Translate

Used the `deep_translator` library to translate the text to Hindi. This library uses the Google Translate API to perform the translations. I used this library as it provides a simple interface to the API and can handle large amounts of text.
### Limits
The Google Translate API have a limit of 5k characters and requests limit of 5 per second and up to 200k requests per day, so to get around this in the Translator class, a glossary/dictionary attribute was created to store the translations so when translating it will lookup if the word or sentence was previously translated and instead of requesting to the Google server it will get the value from there.

## Deployment
Used Vercel to deploy the app 
 
- Minified the HTML files to reduce size and improve size using `html-minifier`
- Minified images to reduce size and improve speed using `@squoosh/cli`
## Improvements

 1. Using Google Cloud Translation service