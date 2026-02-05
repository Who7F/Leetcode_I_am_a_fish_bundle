impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        let mut res = vec![0; nums.len()];
        let (mut left, mut right) = (0, nums.len() - 1);

        for i in (0..nums.len()).rev() {
            if nums[left].abs() > nums[right].abs() {
                res[i] = nums[left] * nums[left];
                left += 1;
            } else {
                res[i] = nums[right] * nums[right];
                right -= 1;
            }
        } 

        res
    }
}