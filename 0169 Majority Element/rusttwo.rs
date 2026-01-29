use std::collections::HashMap;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let counts = nums.into_iter().fold(HashMap::new(), |mut acc, n| {
            *acc.entry(n).or_insert(0) += 1;
            acc
        });

        counts
            .into_iter()
            .max_by_key(|&(_, count)| count)
            .map(|(value, _)| value)
            .unwrap()
    }
}