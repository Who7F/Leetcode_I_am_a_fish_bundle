impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut total = nums[0];
        let mut curr = nums[0];

        for &n in nums.iter().skip(1) {
            curr = n.max(n + curr);
            total = total.max(curr)
        }

        total
    }
}