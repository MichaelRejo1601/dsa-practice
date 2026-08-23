import heapq
class Twitter:

    def __init__(self):
        self.followingMap = defaultdict(set) # userid : set(userid)
        self.tweets = defaultdict(list) # userid : [(count, tweetid)]
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followingMap[userId].add(userId)
        minheap = []
        for poster in self.followingMap[userId]:
            minheap.extend(self.tweets[poster][-10:])
        heapq.heapify(minheap)
        res = []
        while len(res) < 10 and minheap:
            res.append(heapq.heappop(minheap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingMap[followerId]:
            self.followingMap[followerId].remove(followeeId)

    