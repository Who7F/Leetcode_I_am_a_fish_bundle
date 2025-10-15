impl Solution {
    fn dfs(node: usize, state: & mut Vec<i32>, graph: &Vec<Vec<usize>>) -> bool {
        let s = state[node];
        match s {
            2 => return true,
            1 => return false,
            _ => {
                state[node] = 1;
                for &next in &graph[node] {
                    if !Self::dfs(next as usize, state, graph) {
                        return false;
                    }
                }
                state[node] = 2;
                true
            }
        }
    }

    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let mut graph = vec![Vec::new(); num_courses as usize];
        let mut state = vec![0; num_courses as usize];

        for p in prerequisites {
            graph[p[1] as usize].push(p[0] as usize);
        }

        for i in 0..num_courses as usize{
            if !Self::dfs(i, &mut state, &graph) {
                return false;
            }    
        }
        true
    }
}