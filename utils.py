# Helper function to check if a string is completely a number
def is_number(string1: str):
    string = string1.strip()
    for character in string:
        if not character.isdigit():
            return False
    return True


def save_file(file, path: str):
    # open another file for writing
    with open(path, 'w') as fp:
        # write the current soup content
        fp.write(file.prettify())
