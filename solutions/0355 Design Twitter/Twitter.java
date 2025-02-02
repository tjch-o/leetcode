import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.HashSet;
import java.util.HashMap;

class Twitter {
    private HashMap<Integer, HashSet<Integer>> follows;
    private HashMap<Integer, ArrayList<Tweet>> tweets;

    public Twitter() {
        this.tweets = new HashMap<>();
        this.follows = new HashMap<>();
    }
    
    public void postTweet(int userId, int tweetId) {
        if (!tweets.containsKey(userId)) {
            tweets.put(userId, new ArrayList<>());
        }
        tweets.get(userId).add(new Tweet(tweetId));
    }
    
    public List<Integer> getNewsFeed(int userId) {
        PriorityQueue<Tweet> maxHeap = new PriorityQueue<>((a, b) -> Long.compare(b.time, a.time));

        if (tweets.containsKey(userId)) {
            maxHeap.addAll(tweets.get(userId));
        }

        if (follows.containsKey(userId)) {
            for (int followeeId : follows.get(userId)) {
                if (tweets.containsKey(followeeId)) {
                    maxHeap.addAll(tweets.get(followeeId));
                }
            }
        }

        List<Integer> result = new ArrayList<>();

        while (result.size() < 10 && !maxHeap.isEmpty()) {
            Tweet tweet = maxHeap.poll();
            result.add(tweet.tweetId);
        }
        return result;
    }
    
    public void follow(int followerId, int followeeId) {
        if (followerId == followeeId) {
            return;
        }

        if (!follows.containsKey(followerId)) {
            follows.put(followerId, new HashSet<>());
        }
        follows.get(followerId).add(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) {
            return;
        }

        if (!follows.containsKey(followerId)) {
            return;
        }
        follows.get(followerId).remove(Integer.valueOf(followeeId));
    }
}