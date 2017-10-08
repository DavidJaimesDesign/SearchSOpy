#! Python 2.7
# Cli search tool for Stack Overflow

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
else:
    query = pyperclip.paste()

webbrowser.open('https://stackoverflow.com/search?q=' + query)
