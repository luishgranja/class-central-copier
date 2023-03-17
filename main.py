import os
import time

from translator import Translator
from processor import HTMLProcessor

# list_html_files: lists all HTML files in a given directory
def list_html_files(route: str):
    html_files = []
    # Traverse the folder and its subfolders recursively
    for root, dirs, files_ in os.walk(route):
        # Check each file to see if it is an HTML file
        for file in files_:
            if file.endswith(".html") or file.endswith(".htm"):
                html_files.append(os.path.join(root, file))
    return html_files


if __name__ == '__main__':
    t = Translator()
    # List all HTML files in a directory
    files = list_html_files("/home/user/example//www.classcentral.com")
    # Iterate through each file
    for file in files:
        # Create an HTMLProcessor object
        processor = HTMLProcessor(file, t)
        # Process the HTML file
        processor.process_html()
        # Save the processed HTML file
        processor.save_processed_html()
        # Print a message indicating that the file has been completed for logging
        print(file + ' completed')
        # Wait for 5 seconds before processing the next file
        time.sleep(5)
