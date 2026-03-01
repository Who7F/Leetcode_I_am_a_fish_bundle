class Solution {
public:
    int trap(vector<int>& height) {
        int res = 0;
        int left = 0;
        int right = height.size() - 1;
        int h = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                h = max(h, height[left]);
                res += h - height[left];
                left ++;

            } else {
                h = max(h, height[right]);
                res += h - height[right];                
                right --;
            }
        }

        return res;
    }
};