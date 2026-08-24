class User:
    def __init__(self):
        self.follows = set()
        self.tweets = []

    def post_tweet(self, tweet_id: int):
        self.tweets.append(tweet_id)
    
    def follow(self, user: 'User') -> None:
        self.follows.add(user)
    
    def unfollow(self, user: 'User') -> None:
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
        user = self.__users[userId]
        
        heap = []
        followees = list(user.follows) + [user]

        for f in followees:
            if f.tweets:
                idx = len(f.tweets) - 1
                seq_num, t_id = f.tweets[idx]
                heapq.heappush(heap, (-seq_num, t_id, f, idx-1))
        
        res = []
        while heap and len(res) < 10:
            neg_seq_num, t_id, f, idx = heapq.heappop(heap)
            res.append(t_id)

            if idx >= 0:
                next_seq, next_id = f.tweets[idx]
                heapq.heappush(heap, (-next_seq, next_id, f, idx - 1))
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.__users[followerId].follow(self.__users[followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.__users[followerId].unfollow(self.__users[followeeId])