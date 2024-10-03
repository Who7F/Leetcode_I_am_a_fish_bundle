impl Solution {
    pub fn longest_ones(nums: Vec<i32>, k: i32) -> i32 {
        let (mut low, mut cnt) = (0, 0);
        let high = nums.len();

        for h in 0..high{
            if nums[h] == 0{
                cnt += 1;
            }
            if cnt > k{
                if nums[low] == 0{
                    cnt -= 1;
                }
                low += 1;
            }
        }
        (high - low) as i32
    }
}