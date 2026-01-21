use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut seen = HashSet::new();

        for i in 0..9 {
            for j in 0..9 {
                let c = board[i][j];

                if c == '.' {
                    continue;
                }

                if !seen.insert((i, c)) ||
                    !seen.insert((j + 9, c)) ||
                    !seen.insert(((i / 3) * 3 + (j / 3) + 18, c)) {
                        return false;
                    }
            }
        }
        true
    }
}