impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut right = height.len().saturating_sub(1);
        let mut left = 0;

        std::iter::from_fn(|| {
            if left >= right {
                return None;
            }
            
            let width = (right - left) as i32;
            let temp = height[left].min(height[right]) * width;

            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            } 
            Some(temp)

        }).max().unwrap_or(0)       
    }
}