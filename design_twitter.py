from typing import List
from datetime import datetime


class Twitter:
    def __init__(self):
        self.tweets = {}
        self.user_followee = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((tweetId, datetime.now()))

    def getNewsFeed(self, userId: int) -> List[int]:
        all_posts = []
        most_recent_posts = []

        if userId in self.user_followee:
            for followee in self.user_followee[userId]:
                if followee in self.tweets:
                    all_posts.extend(self.tweets[followee])

        if userId in self.tweets:
            all_posts.extend(self.tweets[userId])

        for post in sorted(all_posts, key=lambda x: x[1], reverse=True):
            most_recent_posts.append(post[0])

            if len(most_recent_posts) == 10:
                break

        return most_recent_posts

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_followee:
            self.user_followee[followerId] = []
        if followeeId not in self.user_followee[followerId]:
            self.user_followee[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_followee:
            if followeeId in self.user_followee[followerId]:
                self.user_followee[followerId].remove(followeeId)