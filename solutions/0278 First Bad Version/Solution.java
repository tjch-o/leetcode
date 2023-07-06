public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int start = 1;
        int end = n;

        while (start < end) {
            int middle =  start + (end - start) / 2;
            
            if (isBadVersion(middle) == true) {
                end = middle;
            } else {
                start = middle + 1;
            }
        }
        
        return start;
    }
}