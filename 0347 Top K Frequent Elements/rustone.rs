use std::collections::{BinaryHeap, HashMap};

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut freq_map = HashMap::new();
        let mut heap = BinaryHeap::new();

        for &num in &nums {
            *freq_map.entry(num).or_insert(0) += 1;
        }

        for(&num, &freq) in freq_map.iter() {
            heap.push(std::cmp::Reverse((freq, num)));
            if heap.len() > k as usize {
                heap.pop();
            }
        }
        heap.into_iter().map(|std::cmp::Reverse((_, num))| num).collect()
    }
}