use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn valid_path(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32) -> bool {
        if source == destination {
            return true;
        }
        let mut gph: HashMap<i32, Vec<i32>> = HashMap::new();

        for edge in  edges {
            let (n, m) = (edge[0], edge[1]);

            gph.entry(n).or_insert_with(Vec::new).push(m);
            gph.entry(m).or_insert_with(Vec::new).push(n);
        }

        let mut seen: HashSet<i32> = HashSet::new();
        let mut stack = vec![source];
        
        stack.push(source);

        while !stack.is_empty(){
            let node = stack.pop().unwrap();

            if node == destination {
                return true;
            }

            if let Some(neighbers) = gph.get(&node){
                for &n_node in neighbers {
                    if !seen.contains(&n_node) {
                        seen.insert(n_node);
                        stack.push(n_node);
                    }
                }
            }            
        }
        false
    }
}