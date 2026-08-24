class User:
    def __init__(self):
        self.follows = set()
        self.tweets = []

    def post_tweet(self, tweet_id: int):
        self.tweets.append(tweet_id)
    
    def follow(self, user: User) -> None:
        self.follows.add(user)
    
    def unfollow(self, user: User) -> None:
        if user in self.follows:
            self.follows.remove(user)

class Twitter:

    def __init__(self):
        self.__users = defaultdict(User)
        self.tweet_seq_number = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.__users[userId].post_tweet((self.tweet_seq_number, tweetId))
        self.tweet_seq_number += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        user = self.__users[userId]
        for seq_num, id in user.tweets:
            heapq.heappush(heap, (-seq_num, id))
        
        for follow in user.follows:
            for seq_num, id in follow.tweets:
                heapq.heappush(heap, (-seq_num, id))

        res = []
        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[-1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.__users[followerId].follow(self.__users[followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.__users[followerId].unfollow(self.__users[followeeId])

        
