class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<int> dp(text2.size() + 1, 0);

        for (int i = 0; i < text1.size(); i++) {
            int perv = 0;

            for (int j = 0; j < text2.size(); j++) {
                int temp = dp[j + 1];
                if (text1[i] == text2[j]) {
                    dp[j + 1] = perv +1;
                } else {
                    dp[j + 1] = max(dp[j], dp[j + 1]);
                }
                perv = temp;
            }

        }
        
        return dp.back();
    }
};