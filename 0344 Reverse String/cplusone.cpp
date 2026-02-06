class Solution {
public:
    void reverseString(vector<char>& s) {
        int left = 0;
        int right = s.size() - 1;
        for ( ; ; ) {
            if (left >= right) {
                break;
            }
            int temp = s[right];
            s[right] = s[left];
            s[left] = temp;
            left++;
            right--;    
        }
    }
};