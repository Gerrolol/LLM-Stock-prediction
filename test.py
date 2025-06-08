import ssl
import snscrape.modules.twitter as sntwitter

# This will disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Now proceed with scraping
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('#technology').get_items()):
    print(tweet.content)
