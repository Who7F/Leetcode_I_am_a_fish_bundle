use std::collections::{VecDeque};

#[derive(Clone, Copy, Hash, PartialEq, Eq, Debug)]
struct Pair {
    r: i32,
    c: i32,
}

impl Solution {
    pub fn oranges_rotting(mut grid: Vec<Vec<i32>>) -> i32 {
        let row = grid.len();
        let col = grid[0].len();
        let mut fresh = 0;
        let mut que = VecDeque::new();
        let deltas = [Pair{r: 1, c: 0}, Pair{r: -1, c: 0}, Pair{r: 0, c: 1}, Pair{r: 0, c: -1}];

        for i in 0..row {
            for j in 0..col {
                if grid[i][j] == 2 {
                    que.push_back(Pair{r: i as i32, c: j as i32})
                } else if grid[i][j] == 1 {
                    fresh += 1;
                }
            }
        }

        let mut time = 0;

        while !que.is_empty() {
            let size = que.len();
            for _ in 0..size {
                if let Some(node) = que.pop_front() {
                    for delta in & deltas {
                        let nr = delta.r + node.r;
                        let nc = delta.c + node.c;
                        if nr >= 0 && nr < row as i32 && nc >= 0 && nc < col as i32 && grid[nr as usize][nc as usize] == 1 {
                            grid[nr as usize][nc as usize] = 2;
                            fresh -= 1;
                            que.push_back(Pair{r: nr, c: nc});
                        }
                    }
                }
            }
            if !que.is_empty() {
                time += 1;
            }  
        }
        if fresh == 0 {
            return time;
        }
        -1
    }
}