impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let mut grid: Vec<i32> = vec![1; n as usize];

        for _ in 1..m as usize {
            for j in 1..n as usize {
                grid[j] += grid[j - 1] as i32;
            }
        }

        grid[n as usize - 1]
    }
}