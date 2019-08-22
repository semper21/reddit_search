# In search for interesting observations on Reddit
Bots that crawl through Reddit to extract relevant/interesting information

## Getting started
For each search, there may be specific inputs depending on what the bot is trying to do. 

### Prerequisites
PRAW is the Python Reddit API Wrapper.
```
pip install praw
```
You need a Reddit account (create one at [reddit.com](https://www.reddit.com/)) to access Reddit's API, and client ID and client secret to access Reddit’s API as a ***script*** application. Follow steps [here](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) to create them.

For security purposes, you want to save your account information in a user-created praw.ini file. Follow steps [here](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html). The scripts here use account information from a hidden praw.ini as well. 

