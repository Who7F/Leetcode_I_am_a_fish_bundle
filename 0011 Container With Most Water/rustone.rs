impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = height.len().saturating_sub(1);
        let mut res = 0;

        while left < right {
            let width = right - left;
            let temp = height[left].min(height[right]) * width as i32;
            res = res.max(temp);

            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }
        res
    }
}