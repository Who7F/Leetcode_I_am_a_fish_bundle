use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap};

#[derive(Clone, Copy, Hash, PartialEq, Eq, Debug)]
struct Pair {
    cost: i32,
    node: usize,
}

impl Ord for Pair {
    fn cmp(&self, other: &Self) -> Ordering {
        other.cost.cmp(&self.cost)
    }
}

impl PartialOrd for Pair {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn min_cost_connect_points(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        if n == 0 {
            return 0;
        }
        let mut heap = BinaryHeap::new();
        let mut seen = HashMap::new();
        let mut cost = 0;

        heap.push(Pair{cost: 0, node: 0});
        
        
        while let Some(Pair {cost: node_cost, node}) = heap.pop() {  
            if seen.contains_key(&node) {
                continue;
            }
            cost += node_cost;
            seen.insert(node, true);
                
            for nei in 0..n {
                if !seen.contains_key(&nei) {
                    let next_cost = (points[node][0] - points[nei][0]).abs() + (points[node][1] - points[nei][1]).abs(); 
                    heap.push(Pair{cost: next_cost, node: nei});
                }
            }
            if seen.len() == n {
                break;
            }
        }
        cost
    }
}