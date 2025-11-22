impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut maxJump = 0;

        for i in 0..nums.len() {
            if i > maxJump {
                return false
            }
            maxJump = maxJump.max(i+ nums[i] as usize)
        }
        true   
    }
}