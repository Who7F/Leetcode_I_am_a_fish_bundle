use std::collections::HashMap;

#[derive(Clone, Copy, Hash)]
struct Pair {
    first: i32,
    second: i32,
}

impl Solution {
    pub fn minimum_distance(nums: Vec<i32>) -> i32 {
        let mut seen: HashMap<i32, Pair> = HashMap::new();
        let mut min_total = i32::MAX;

        for (idx, num) in nums.into_iter().enumerate() {
            if let Some(pair) = seen.get_mut(&num) {
                if pair.first != i32::MAX {
                    min_total = min_total.min((idx as i32 - pair.first) * 2);
                }
                pair.first = pair.second;
                pair.second = idx as i32;
            } else {
                seen.insert(num, Pair { first: i32::MAX, second: idx as i32 });
            }
        }

        if min_total == i32::MAX {
            -1
        } else {
            min_total
        }
    }
}