impl Solution {
    fn get_island(i: i32, j: i32, grid: &mut Vec<Vec<i32>>, deltas: &[(i32, i32)]) -> i32 {
        if i < 0 || i >= grid.len() as i32 || j < 0 || j >= grid[0].len() as i32 || grid[i as usize][j as usize] == 0{
            return 0
        }

        grid[i as usize][j as usize] = 0;
        let mut res = 1; 

        for (di, dj) in deltas.iter(){
            res += Self::get_island(i+ di, j + dj, grid, &deltas);
        }
        res
    }

    pub fn max_area_of_island(mut grid: Vec<Vec<i32>>) -> i32 {
        if grid.is_empty() {
            return 0;
        }
        let rows = grid.len();
        let cols = grid[0].len();
        let mut res = 0;
        let deltas = vec![(1, 0), (-1, 0), (0, 1), (0, -1)];

        for i in 0..rows{
            for j in 0..cols{
                res = res.max(Self::get_island(i as i32, j as i32, &mut grid, &deltas));
            }
        }

        res
    }
}