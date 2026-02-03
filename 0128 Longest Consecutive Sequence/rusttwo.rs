use std::collections::HashSet;

fn length_from(n: i32 , set: &HashSet<i32>) -> i32 {
    if set.contains(&(n + 1)) {
        1 + length_from(n + 1, set)
    } else {
        1
    }
}

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {

        let set: HashSet<i32> = nums.into_iter().collect();

        set.iter()
           .filter(|&&n| !set.contains(&(n - 1)))
           .map(|&n| length_from(n, &set))
           .max()
           .unwrap_or(0)
    }
}