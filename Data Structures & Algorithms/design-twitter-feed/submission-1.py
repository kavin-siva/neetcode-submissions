from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        # Maps userId -> set of followeeIds
        self.follow_map = defaultdict(set)
        # Maps userId -> list of pairs: [time, tweetId]
        self.tweet_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # We decrement time because Python's heapq is a min-heap by default.
        # This allows us to sort by the most recent (smallest negative value) first.
        self.tweet_map[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        min_heap = []
        
        # Ensure a user always "follows" themselves to see their own tweets
        self.follow_map[userId].add(userId)
        
        # Gather the most recent tweet index from the user and everyone they follow
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                tweets = self.tweet_map[followeeId]
                last_idx = len(tweets) - 1
                time, tweetId = tweets[last_idx]
                # Store: (time, tweetId, followeeId, next_index_to_look_at)
                min_heap.append((time, tweetId, followeeId, last_idx - 1))
                
        # Convert list into a valid heap structure
        heapq.heapify(min_heap)
        
        # Pull up to 10 most recent tweets
        while min_heap and len(res) < 10:
            time, tweetId, followeeId, next_idx = heapq.heappop(min_heap)
            res.append(tweetId)
            
            # If the user has older tweets left, push the next one onto the heap
            if next_idx >= 0:
                next_time, next_tweetId = self.tweet_map[followeeId][next_idx]
                heapq.heappush(min_heap, (next_time, next_tweetId, followeeId, next_idx - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)


        
