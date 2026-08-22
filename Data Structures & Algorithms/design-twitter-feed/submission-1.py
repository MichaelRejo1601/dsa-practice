class Twitter:

    def __init__(self):

        self.following_set_for = {} # set()
        self.tweet_timeline = [] # (user_id, tweet_id)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.check_and_init_user(userId)

        self.tweet_timeline.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.check_and_init_user(userId)

        feed = []
        i = -1
        while len(feed) < 10 and i > -1 * (len(self.tweet_timeline) + 1):
            if self.tweet_timeline[i][0] in self.following_set_for[userId]:
                feed.append(self.tweet_timeline[i][1]) # add tweet if the poster is in the following list
            i -= 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.check_and_init_user(followerId)

        self.following_set_for[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.check_and_init_user(followerId)

        if followeeId in self.following_set_for[followerId]:
            self.following_set_for[followerId].remove(followeeId)


    def check_and_init_user(self, userid):
        if userid not in self.following_set_for:
            self.following_set_for[userid] = set([userid])

        
