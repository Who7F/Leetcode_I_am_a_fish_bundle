use std::collections::{HashSet, VecDeque};

#[derive(Clone, Copy, Hash, PartialEq, Eq, Debug)]
struct Pair {
    r: i32,
    c: i32,
}

impl Solution {
    fn bfs(heights: &Vec<Vec<i32>>, que: &mut VecDeque<Pair>) -> HashSet<Pair>{
        let row = heights.len() as i32;
        let col = heights[0].len() as i32;

        let deltas = [Pair{r: 1, c: 0}, Pair{r: -1, c: 0}, Pair{r: 0, c: 1}, Pair{r: 0, c: -1}];

        let mut seen = HashSet::new();

        while let Some(node) = que.pop_front() {
            if seen.contains(&node) {
                continue;
            }
            seen.insert(node);

            for d in & deltas {
                let nr = d.r + node.r;
                let nc = d.c + node.c;

                if nr >= 0 && nr < row && nc >= 0 && nc < col && heights[nr as usize][nc as usize] >= heights[node.r as usize][node.c as usize] {
                    que.push_back(Pair{r: nr, c: nc});
                }
            }
        }
        seen
    }

    pub fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        if heights.is_empty() { return vec![]; }

        let row = heights.len();
        let col = heights[0].len();

        let mut pacific = VecDeque::new();
        let mut atlantic = VecDeque::new();

        for i in 0..row {
            pacific.push_back(Pair {r: i as i32, c: 0});
            atlantic.push_back(Pair {r: i as i32, c: (col - 1) as i32});
        }

        for j in 0..col {
            pacific.push_back(Pair {r: 0, c: j as i32});
            atlantic.push_back(Pair {r: (row - 1) as i32, c: j as i32});
        }

        let pac_set = Self::bfs(&heights, &mut pacific);
        let atl_set = Self::bfs(&heights, &mut atlantic);

        let mut res = vec![];

        for node in pac_set.intersection(&atl_set) {
            res.push(vec![node.r, node.c]);
        }

        res 
    }
}