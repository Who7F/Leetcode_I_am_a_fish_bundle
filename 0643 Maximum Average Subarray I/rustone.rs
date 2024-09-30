impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let(mut total, top) = (0, nums.len());

        for i in 0..k{
            total += nums[i as usize];
        }

        let mut anc = total;

        for i in k..top as i32{
            total += nums[i as usize];
            total -= nums[(i - k) as usize];
            anc = std::cmp::max(anc, total);
        } 
    anc as f64/k as f64
    }
}