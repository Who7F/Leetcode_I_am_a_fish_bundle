class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    int ans = 0;
    vector<int> count(128);
    int l = 0;
    for (int r = 0; r < s.length(); ++r) {  
        count[s[r]] ++;
        while (count[s[r]] > 1)
            count[s[l++]] --;
        cout << r - l + 1;
        ans = max(ans, r - l + 1);
    }
    return ans;
  }
};