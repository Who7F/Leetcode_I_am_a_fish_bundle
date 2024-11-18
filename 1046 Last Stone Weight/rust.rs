use std::collections::BinaryHeap;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut s = BinaryHeap::from(stones);
        while !s.is_empty() {
            match (s.pop(), s.pop()) {
                (Some(a), Some(b)) if a > b => s.push(a - b),
                (Some(a), None) => return a,
                _ => (),
            } 
        }
        0
    }
}