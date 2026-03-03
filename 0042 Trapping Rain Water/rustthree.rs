impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = height.len().saturating_sub(1);
        let mut res = 0;
        let mut h = 0;

        while left < right {
            if height[left] < height[right] {
                h = h.max(height[left]);
                res += h - height[left];
                left += 1;
            } else {
                h = h.max(height[right]);
                res += h - height[right];
                right -= 1;
            }
        }

        res
    }
}