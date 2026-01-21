use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut seen = HashSet::new();

        board.iter().enumerate().all(|(i, row)| {
            row.iter().enumerate().all(|(j, &c)| {
                if c == '.' {
                    true
                } else {
                    seen.insert((i, c)) &&
                    seen.insert((j + 9, c)) &&
                    seen.insert(((i / 3) * 3 + (j / 3) + 18, c))
                }
            })
        })
    }
}