impl Solution {
    fn get_max(left: usize, right: usize, res: i32, height: &Vec<i32>) -> i32 {
        if left >= right {
            return res;
        }

        let width = (right - left) as i32;
        let temp = height[left].min(height[right]) * width;
        let new_res = res.max(temp);

        match height[left] < height[right] {
            true => Self::get_max(left + 1, right, new_res, height),
            false => Self::get_max(left, right - 1, new_res, height),
        }
    }

    pub fn max_area(height: Vec<i32>) -> i32 {
        let right = height.len().saturating_sub(1);
        Self::get_max(0, right, 0, &height)
    }
}