public class Tweet {
    public int tweetId;
    public static long timestamp = 0;
    public long time;

    public Tweet(int tweetId) {
        this.tweetId = tweetId;
        time = timestamp;
        timestamp++;
    }
}
