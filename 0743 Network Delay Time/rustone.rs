use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap};

#[derive(Clone, Copy, Hash, PartialEq, Eq, Debug)]
struct Pair {
    time: i32,
    node: usize,
}

impl Ord for Pair {
    fn cmp(&self, other: &Self) -> Ordering {
        other.time.cmp(&self.time)
    }
}

impl PartialOrd for Pair {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn network_delay_time(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        let mut graph: HashMap<usize, Vec<Pair>> = HashMap::new(); //: HashMap<usize, Vec<Pair>> isn't needed

        for time in times.iter() {
            let (u, v, w) = (time[0] as usize, time[1] as usize, time[2]);
            graph.entry(u).or_insert(Vec::new()).push(Pair{time: w, node: v})    
        }

        let mut heap = BinaryHeap::new();
        let mut dist = HashMap::new();

        heap.push(Pair{time: 0, node: k as usize});

        while let Some(Pair {time: node_time, node}) = heap.pop() {
            if dist.contains_key(&node) {
                continue;
            }
            dist.insert(node, node_time);

            if let Some(neighbors) = graph.get(&node) {
                for nei in neighbors {
                    if !dist.contains_key(&nei.node) {
                        heap.push(Pair {time: node_time + nei.time, node: nei.node});
                    }
                }
            }       
        }
        
        if dist.len() != n as usize {
            return -1
        }
        *dist.values().max().unwrap()
    }
}