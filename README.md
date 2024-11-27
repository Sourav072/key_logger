# Keylogger with Telegram Integration

A Python-based keylogger that logs keystrokes and sends them to a Telegram chat at regular intervals.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to install and run the keylogger project:

1. Clone the repository:
   ```bash
   git clone https://github.com/Sourav072/key_logger.git
   ```

2. Navigate to the project directory:
   ```bash
   cd key_logger
   ```

3. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install pynput requests
   ```

5. Configure the script by replacing `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` with your Telegram bot token and chat ID in the script file.

6. Run the application:
   ```bash
   python keylogger.py
   ```

## Usage

- The keylogger logs all keystrokes and saves them to a local file (`google.txt`).
- It sends the logged data to a specified Telegram chat at regular intervals (default: every 60 seconds).
- To stop the keylogger, press the `Esc` || `Cntrl + c` key.

## Features

- Logs all keyboard activity.
- Sends logs to a Telegram chat at a configurable interval.
- Clears the local log file after successfully sending the logs.
- Runs in the background until stopped by the user.

## Technologies Used

- [Python](https://www.python.org): Programming language.
- [pynput](https://pypi.org/project/pynput/): Library to monitor keyboard inputs.
- [requests](https://pypi.org/project/requests/): Library for sending HTTP requests.
- [Telegram Bot API](https://core.telegram.org/bots): For communication with Telegram.

## Contributing

If you'd like to contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
