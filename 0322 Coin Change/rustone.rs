impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let a = amount as usize;

        let mut dp: Vec<i32> = vec![amount + 1; a + 1];

        dp[0] = 0;

        for i in 1..(a+1) {
            
            for &c in coins.iter() {
                if i >= c as usize {
                    dp[i] = dp[i].min(dp[i - c as usize] + 1);
                }
            }
        } 
        if dp[a] > amount { -1 } else {dp[a]}
    }
}