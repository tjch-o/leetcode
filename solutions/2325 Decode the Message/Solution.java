import java.util.HashMap;

class Solution {
    public String decodeMessage(String key, String message) {
        HashMap<Character, Character> firstOccurenceMap = new HashMap<>();
        char ptr = 'a';

        for (int i = 0; i < key.length(); i += 1) {
            char curr = key.charAt(i);
            if (curr != ' ' && !firstOccurenceMap.containsKey(curr)) {
                firstOccurenceMap.put(key.charAt(i), ptr);
                ptr += 1;
            }
        }

        StringBuilder res = new StringBuilder();
        for (int i = 0; i < message.length(); i += 1) {
            if (message.charAt(i) == ' ') {
                res.append(' ');
            } else {
                res.append(firstOccurenceMap.get(message.charAt(i)));
            }
        }
        return res.toString();
    }
}