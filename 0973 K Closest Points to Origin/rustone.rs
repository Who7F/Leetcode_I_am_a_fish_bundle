use std::collections::BinaryHeap;

impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let mut heap = BinaryHeap::new();

        for p in &points {
            let destance = p[0] * p[0] + p[1] * p[1];
            heap.push((destance, p.clone()));

            if heap.len() > k as usize {
                heap.pop();
            }
        }
        heap.into_iter().map(|(_, point)| point).collect()
    }
}