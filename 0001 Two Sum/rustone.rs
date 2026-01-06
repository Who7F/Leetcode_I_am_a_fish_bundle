use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::new();

        for (i, &n) in nums.iter().enumerate() {
            let need = target - n;

            if let Some(&idx) = seen.get(&need) {
                return vec![idx as i32, i as i32];
            } else {
                seen.insert(n, i);
            }
        }
        vec![]    
    }
}