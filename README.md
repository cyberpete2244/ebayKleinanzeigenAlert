# kleinanzeigenAlert - (ebAlert)
Small CLI program that will send you a Telegram message for every new posts on the specific links of the Kleinanzeigen and to some extent Ebay websites. 

This is a fork from [vinc3PO/ebayKleinanzeigenAlert](https://github.com/vinc3PO/ebayKleinanzeigenAlert)

No API required - Only URL of the query.

## Install

1. Clone this repository
   ```sh
   git clone https://github.com/cyberpete2244/kleinanzeigenAlert
   ```
2. Navigate to the cloned repository
   ```sh
   cd kleinanzeigenAlert
   ```
3. Create a Telegram Bot
   1. Open the chat with [@BotFather](https://t.me/BotFather)
   2. Enter `/newbot`
   3. Enter the name of your Bot (e.g. Kleinanzeigen Bot)
   4. Enter an unique username for your bot (e.g. my_kleinanzeigen_bot)
   5. Copy the token
4. Get you Telegram Message ID
   1. Open the chat with [@RawDataBot](https://t.me/RawDataBot)
   2. Enter `/start`
   3. Copy the message ID. Either from `message/from/id` or `message/chat/id`. The message ID looks like `417417807`.
5. Set environment variables TOKEN and CHAT_ID. Or hard code your token & message ID in `ebAlert/core/config.py`.
6. Start a conversation with the bot from your Telegram App, otherwise the Telegram Bot cannot contact you.
7. Install the dependencies
   ```sh
   pip install .
   ```
8. Run the `ebAlert` CLI
   ```sh
   python3 -m ebAlert
   ```

## Usage & Example
I removed the ability to add searches using CLI, might add it back later. Currently one need to set up searches using SQL queries directly in DB or by using any third party SQL manager (e.g. SQLite3). 
* ```ebAlert start [opts] ``` to run script with options
* ```ebAlert start --help ``` to get list of options
  
* ```ebAlert start ``` to start receiving notification or generally use this in a cronjob

* Typically, this would be run as a cron job on an hourly basis.

## Creating Searches (TODO)
search types (Kleinanzeigen URLS) need to be defined in DB. They and are templates for arguments for Kleinanzeigen searches in a subdomain format. (e.g. "/s-spielzeug/anbieter:privat/anzeige:angebote/{NPAGE}{SEARCH_TERM}k0c23")
* parameter in these templates is
* {SEARCH_TERM}: This is the placeholder for pagination and an actual search string to narrow Kleinanzeigen searches 

## Requirements
* A telegram bot API token and your personal conversation ID
* ScrapeOPS API token
* Python 3
* Libraries
  * click
  * requests
  * bs4
  * sqlalchemy
  * bs4
  * beautifulsoup4
  * geopy
  * setuptools
  * scrapeops-scrapy

## ChangeLog
  1.2 (forked) -> 2.0
* Database rework
* Searches are added in DB directly
* Items filtering by distance possible. Distance can be defined globally or per search.
* Headers for scraper are generated randomly using ScrapeOPS API
* Searching Ebay is possible. Matching of items to Kleinanzeigen searches is consequent executions

## Future Plans

* add functionality to interact with script via telegram.
