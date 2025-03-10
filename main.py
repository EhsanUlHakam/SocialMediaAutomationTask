import os
from typing import List, Dict
import logging

try:
    import praw
    from dotenv import load_dotenv
except ImportError as e:
    print("Required packages are missing. Please run these commands in your terminal:")
    print("pip install praw python-dotenv")
    raise SystemExit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RedditPostFetcher:
    def __init__(self):
        """Initialize Reddit API client using credentials from .env file"""
        if not os.path.exists('.env'):
            logger.error("'.env' file not found. Please create one from '.env.example' template")
            raise FileNotFoundError("Missing .env file")

        load_dotenv()
        try:
            self.reddit = praw.Reddit(
                client_id=os.getenv('REDDIT_CLIENT_ID'),
                client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                user_agent=os.getenv('REDDIT_USER_AGENT', 'Python/PRAW Latest Posts Fetcher v1.0')
            )
            logger.info("Successfully initialized Reddit client")
        except Exception as e:
            logger.error(f"Failed to initialize Reddit client: {str(e)}")
            raise

    def get_latest_posts(self, subreddit_name: str, limit: int = 5) -> List[Dict]:
        """
        Fetch the latest posts from a specified subreddit

        Args:
            subreddit_name (str): Name of the subreddit to fetch posts from
            limit (int): Number of posts to fetch (default: 5)

        Returns:
            List[Dict]: List of posts with title, author, and upvote count
        """
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            posts = []

            for post in subreddit.new(limit=limit):
                post_data = {
                    'title': post.title,
                    'author': str(post.author),
                    'upvotes': post.score
                }
                posts.append(post_data)

            logger.info(f"Successfully fetched {len(posts)} posts from r/{subreddit_name}")
            return posts

        except praw.exceptions.PRAWException as e:
            logger.error(f"PRAW error occurred: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error occurred: {str(e)}")
            raise

def main():
    """Main function to demonstrate the Reddit post fetcher"""
    try:
        # Initialize the post fetcher
        post_fetcher = RedditPostFetcher()

        # Specify the subreddit to fetch posts from
        subreddit_name = "Python"  # You can change this to any subreddit

        # Fetch and display the posts
        posts = post_fetcher.get_latest_posts(subreddit_name)

        print(f"\nLatest posts from r/{subreddit_name}:")
        print("-" * 50)

        for i, post in enumerate(posts, 1):
            print(f"\nPost #{i}")
            print(f"Title: {post['title']}")
            print(f"Author: u/{post['author']}")
            print(f"Upvotes: {post['upvotes']}")
            print("-" * 50)

    except Exception as e:
        logger.error(f"Failed to fetch posts: {str(e)}")
        raise

if __name__ == "__main__":
    main()