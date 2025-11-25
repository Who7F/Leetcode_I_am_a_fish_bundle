impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut dp: Vec<i32> = vec![nums[0]];

        for &n in nums.iter().skip(1) {
            if n > *dp.last().unwrap() {
                dp.push(n);
            } else {
                let idx = match dp.binary_search(&n) {
                    Ok(i) => i,
                    Err(i) => i,
                };
                dp[idx] = n;
            }
        }
    dp.len() as i32
    }
}