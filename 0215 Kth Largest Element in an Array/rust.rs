use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut heap = BinaryHeap::from(nums[..k].iter().map(|&x| Reverse(x)).collect::<Vec<_>>());

        for &num in &nums[k..]{
            if let Some(&Reverse(top)) = heap.peek() {
                if num > top{
                    heap.pop();
                    heap.push(Reverse(num));
                }
            }
        }
        heap.peek().map(|x| x.0).unwrap_or(0)
    }
}