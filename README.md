# Reddit Latest Posts Fetcher

This Python script demonstrates interaction with the Reddit API to fetch the latest posts from a specified subreddit using PRAW (Python Reddit API Wrapper).

## Features
- OAuth authentication with Reddit API
- Fetches 5 latest posts from a specified subreddit
- Displays post title, author, and upvote count
- Includes error handling and logging
- Uses environment variables for secure credential management

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the script files

2. Install required dependencies:
```bash
pip install praw python-dotenv
```

3. Create a `.env` file in the same directory as the script with your Reddit API credentials:
```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=Python/PRAW Latest Posts Fetcher v1.0
```

To obtain Reddit API credentials:
1. Visit https://www.reddit.com/prefs/apps
2. Click "create application"
3. Select "script"
4. Fill in the required information
5. Once created, you'll get the client_id and client_secret
6. Create a `.env` file:
   - Copy `.env.example` to `.env`
   - Fill in your Reddit API credentials


## Usage

Run the script using Python:
```bash
python main.py
```

## Features

- Fetches the 5 latest posts from a specified subreddit
- Displays post title, author, and upvote count
- Includes error handling and logging
- Uses environment variables for secure credential management


## Error Handling

The script includes comprehensive error handling for:
- API authentication failures
- Network errors
- Invalid subreddit names
- General exceptions

## Logging

Logs are printed to the console with timestamps and appropriate log levels.