import tweepy
from tracardi_twitter_tweet.model.model import TwitterCredentials


class TwitterClient:
    def __init__(self, credentials: TwitterCredentials):
        self.credentials = credentials
        auth = tweepy.OAuthHandler(
            self.credentials.consumer_key,
            self.credentials.consumer_secret
        )
        auth.set_access_token(
            self.credentials.access_token,
            self.credentials.access_token_secret
        )
        self.api = tweepy.API(auth)
        self.api.verify_credentials()

    async def tweet(self, message):
        return self.api.update_status(status=message)

    async def send_direct_message(self, to, message):
        user = self.api.get_user(screen_name=to)
        return self.api.send_direct_message(user.id_str, message)

    # async def auto_follow_followers(self):
    #     for follower in self.api.get_followers():  # type: User
    #         if not follower.following:
    #             follower.follow()
    #             asyncio.sleep(0)
    #             # todo yield followed screen_Names
    #
    # async def get_user(self, screen_name) -> TwitterUser:
    #     user = self.api.get_user(screen_name=screen_name, include_entities=False)
    #     return TwitterUser(
    #         id=user.id,
    #         screen_name=user.screen_name,
    #         location=user.location,
    #         lang=user.lang,
    #         description=user.description
    #     )
    #
    # async def like_all_mentions(self):
    #     tweets = self.api.mentions_timeline()
    #     for tweet in tweets:  # type: Status
    #         if not tweet.favorited:
    #             tweet.favorite()
    #             asyncio.sleep(0)
    #             # todo yield list of texts and users
    #             print(tweet.text)