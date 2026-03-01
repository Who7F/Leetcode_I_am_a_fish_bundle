//This code is using a pointer for no good reason. I just wanted to make some bad code

class Solution {
public:
    int* magic(vector<int>& height, int &n, int m, int mod) {
        int* cnt = new int(0); 
        while (n >= 0 && n < height.size() && height[n] <= m) {  // Add bounds checking for `n`
            *cnt = *cnt + m - height[n];
            n = n + mod;
        }
        return cnt;
    }

    int trap(vector<int>& height) {
        int cnt = 0;
        int lo = 0;
        int hi = height.size() - 1;
        int m = height[lo];
        if (m > height[hi])
            m = height[hi];

        while (lo < hi) {
            if (height[lo] <= m) {
                m = height[lo];
                int* tempCnt = magic(height, lo, m, 1);
                cnt += *tempCnt;
                delete tempCnt;
            } else {
                m = height[hi];
                int* tempCnt = magic(height, hi, m, -1);
                cnt += *tempCnt;
                delete tempCnt;
            }
        }

        return cnt;
    }
};