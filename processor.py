from bs4 import BeautifulSoup, NavigableString, Tag

from translator import Translator
from utils import is_number, save_file


class HTMLProcessor:
    def __init__(self, filename, t):
        self.filename = filename
        self.t = t
        # Opening and reading the HTML file
        with open(filename, 'r') as f:
            self.html = f.read()
        # Parsing HTML into BeautifulSoup object
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def process_element(self, element):
        # Skip script and style tags
        if element.name in ['script', 'style']:
            return

        # If the element has children, process them recursively
        if isinstance(element, Tag):
            for child in element.contents:
                self.process_element(child)
        # If the element is a string, process the text
        elif isinstance(element, NavigableString):
            text = element.get_text().strip()
            # Ignore if it is a number or no text or empty string
            if len(text) > 0 and not is_number(text):
                # Replace original text with translated text
                element.string.replace_with(self.t.translate(element.string.strip()) or '')

    def process_html(self):
        # Process the HTML recursively
        for element in self.soup.contents:
            self.process_element(element)

    # save_processed_html: saves the modified HTML
    def save_processed_html(self):
        save_file(self.soup, self.filename)
        return self.soup.prettify()
