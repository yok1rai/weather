# Weather

![Python](https://img.shields.io/badge/Python-3.10+-blue)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/license/mit)
[![Author](https://img.shields.io/badge/Author-yok1rai-brown?logo=github)](https://github.com/yok1rai)

A simple Python project to fetch and display weather information for any city. Requires an internet connection and an OpenWeatherMap API key.

---

## Features

- Start a local server to handle weather requests.
- Command-line interface (CLI) for querying weather.
- Fetches temperature, humidity, wind speed, and general weather description.
- Cross-platform support for clearing the console.
- Handles errors gracefully.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yok1rai/weather.git
cd weather
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Set your OpenWeatherMap API key in an environment variable

```bash
export API_KEY="your_api_key_here" # Linux/macOS
setx API_KEY "your_api_key_here" # Windows
```

---

## Usage

### Run the CLI

```bash
python -m weather.main
```

You can optionally pass a city as an argument

```bash
python -m weather.main London
```

Or enter cities interactively

```Python
Enter the city (or 'exit' to quit): Tokyo
city: Tokyo
Weather is clear sky
Temperature is 24°C
Humidity level is 60%
Lastly, the wind speed is 5 m/s
```

### Start the server

The CLI automatically starts a local Flask server on `http://127.0.0.1:5000`

You can also start the server manually

```bash
python -m weather.server
```

Access the API endpoint:

```bash
GET http://127.0.0.1:5000/weather?city=London
```

---

## Project Structure

```text
weather/
├── src
│   └── weather
│       ├── main.py         # CLI entry point
│       ├── network.py      # handles API requests
│       ├── server.py       # flask server providing weather data
│       └── utils.py        # utility functions (console clear, etc..)
├── .gitignore
├── license
├── pyproject.toml
└── README.md
```

---

## Dependencies

- `requests`    — for making HTTP requests
- `flask`       — for running the local server
- `dotenv`      — for environment variable management

optional (for development):

- `pytest`      — for testing
- `black`       — for code formatting
- `mypy`        — for type checking

---

## License

This project is licensed under the [MIT license](https://github.com/yok1rai/weather/blob/main/license). See [LICENSE](https://opensource.org/license/mit) for details
