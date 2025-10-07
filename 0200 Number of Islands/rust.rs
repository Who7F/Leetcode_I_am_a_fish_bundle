impl Solution {
    fn getIslands(i: i32, j: i32, grid: &mut Vec<Vec<char>>, deltes: &[(i32, i32)]){
        let mut stack = vec![(i, j)];
        let row = grid.len() as i32;
        let col = grid[0].len() as i32;


        while let Some((x, y)) = stack.pop(){
            if x >= 0 && x < row && y >= 0 && y < col{
                if grid[x as usize][y as usize] == '1'{
                    grid[x as usize][y as usize] = '0';
                    for (dx, dy) in deltes.iter(){
                        stack.push((x + dx, y + dy));
                    }
                }
            }
        }
    }

    pub fn num_islands(mut grid: Vec<Vec<char>>) -> i32 {
        if grid.is_empty() {
            return 0;
        }

        let deltas = vec![(1, 0), (-1, 0), (0, 1), (0, -1)];
        let mut islands :i32 = 0;
        let rows = grid.len();
        let cols = grid[0].len();

        for i in 0..rows{
            for j in 0..cols{
                if grid[i][j] == '1'{
                    islands += 1;
                    Self::getIslands(i as i32, j as i32, &mut grid, &deltas);
                }
            }
        }
        islands
    }
}