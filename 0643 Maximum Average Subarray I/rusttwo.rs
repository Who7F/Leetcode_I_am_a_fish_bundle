impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let(k, top) = (k as usize, nums.len());

        let mut total = nums.iter().take(k).sum::<i32>();

        let mut anc = total;

        for i in k..top{
            total += nums[i]- nums[(i - k)];
            anc = anc.max(total);
        } 
    anc as f64/k as f64
    }
}