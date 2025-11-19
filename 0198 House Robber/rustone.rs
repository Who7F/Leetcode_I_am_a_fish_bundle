impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return nums[0];
        }

        let (mut prev2, mut prev1) = (nums[0], nums[1]);

        for n in &nums[2..] {
            (prev2, prev1) = (prev2.max(prev1), prev2 + n);
        }
        
        prev2.max(prev1)
    }
}