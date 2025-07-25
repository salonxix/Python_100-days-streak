# Install pyfiglet before running: pip install pyfiglet
import pyfiglet

def ascii_art(text):
    ascii_banner = pyfiglet.figlet_format(text)
    print(ascii_banner)

if __name__ == "__main__":
    name = input("Enter your name or any word: ")
    ascii_art(name)
