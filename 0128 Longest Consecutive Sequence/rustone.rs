use std::collections::HashSet;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        let set: HashSet<i32> = nums.into_iter().collect();

        for &s in set.iter() {
            if !set.contains(&(s - 1)) {
                let mut length = 1;
                while set.contains(&(s + length)) {
                    length += 1;
                }
                res = res.max(length)
            }
        }
        res
    }
}
