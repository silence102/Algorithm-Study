class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        String[] my = my_string.split("");
        String[] over = overwrite_string.split("");
        for (int i = 0; i < s; i++) {
            answer += my[i];
        }
        for (int i = 0; i < over.length; i++) {
            answer += over[i];
        } 
        for (int i = s + over.length; i < my.length; i++) {
            answer += my[i];
        }
        return answer;
    }
}