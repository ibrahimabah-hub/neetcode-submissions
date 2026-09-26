class Twitter:
    class User:
        def __init__(self, userId):
            self.userId = userId
            self.following = [self.userId]
            self.tweets = []
        
    def __init__(self):
        self.users = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        if userId not in self.users:
            user = self.User(userId)
            self.users[userId] = user
        else:
            user = self.users[userId]

        user.tweets.append([self.time, tweetId])
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.users[userId].following
        tweets = []
        heap = []
        for follow in following:
            user = self.users[follow]
            for tweet in user.tweets:
                heapq.heappush_max(heap, tweet)
        while heap and len(tweets)<10:
            _, tweet = heapq.heappop_max(heap)
            tweets.append(tweet)
        
        return tweets
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = self.User(followerId)
        user1 = self.users[followerId]
        if followeeId not in user1.following:
            user1.following.append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user1 = self.users[followerId]
        if followeeId in user1.following:
            user1.following.remove(followeeId)
        
