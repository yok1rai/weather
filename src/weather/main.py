from weather.network import show
from weather.utils import cls
import sys

def main():
    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
        print(show(city))
    else:
        while True:
            city = input("Enter the city (or 'exit' to quit): ").strip()
            cls()
            if city.lower() in ('exit', 'quit'):
                print('Goodbye!')
                break
            print(show(city))

if __name__ == "__main__":
    main()
