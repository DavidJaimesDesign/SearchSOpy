#! Python 2.7
# Cli search tool for Stack Overflow
try:
    import webbrowser
    import sys
    import pyperclip
except ImportError:
    print("""
Please install dependencies:
    pip install -U webbrowser pyperclip 
            """)
    raise

def main():
    """
    This is the main function that is called in this script 
    """
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
    else:
        query = pyperclip.paste()

    webbrowser.open('https://stackoverflow.com/search?q=' + query)

if __name__=='__main__':
    main()
