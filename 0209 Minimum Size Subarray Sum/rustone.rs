impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let (mut low, mut ttl) = (0, 0);
        let mut anc = i32::MAX;

        for i in 0..nums.len(){
            ttl += nums[i];
            while ttl >= target{
                anc = anc.min(i as i32 - low + 1);
                ttl -= nums[low as usize];
                low += 1;
            }
        }
        if anc == i32::MAX {0} else {anc}
    }
}