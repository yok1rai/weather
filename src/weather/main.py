from weather.network import show
from weather.utils import cls
import threading
import sys
from weather import server

def start_server():
    server.app.run(debug=False, port=5000, use_reloader=False)

def main():
    threading.Thread(target=start_server, daemon=True).start()

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
