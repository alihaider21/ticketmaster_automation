# Ticketmaster Bot

Automate the process of buying event tickets on Ticketmaster Italy using this Python script. The script interacts with the Ticketmaster website, allowing you to automatically search for events, purchase tickets, and receive notifications via Telegram when tickets are available.

## Features

- **Automated Login:** The script logs in to your Ticketmaster Italy account using provided credentials.
- **Event Search:** Specify a list of artist names, and the script will search for upcoming events for each artist.
- **Ticket Purchasing:** The script attempts to purchase tickets for available events, handling ticket quantity selection, e-tickets, and recaptcha challenges.
- **Telegram Notifications:** Receive notifications in a Telegram chat when tickets are available.

## Prerequisites

Before using the script, ensure you have the following prerequisites:

- Python 3.x
- Selenium (`pip install selenium`)
- Chrome WebDriver (for Selenium) compatible with your Chrome browser version
- Fake User-Agent (`pip install fake-useragent`)
- Telegram Bot API token and chat ID

## Configuration

1. Replace the `email` and `password` values in the `login_dict` dictionary with your Ticketmaster Italy account credentials.
2. Add artist names to the `artist_list` to specify the events you're interested in.
3. Set the `telegram_id` variable with your Telegram chat ID.
4. Replace `apiToken` with your Telegram Bot API token in the `send_to_telegram` function.

## Usage

1. Install the required libraries using the provided prerequisites.
2. Download and install the appropriate Chrome WebDriver for your Chrome browser version.
3. Configure the script as mentioned above.
4. Run the script using the command `python ticketmaster_bot.py`.

Please note that the script might need adjustments based on website changes or CAPTCHA handling. Use it responsibly and in accordance with Ticketmaster's terms of use.
