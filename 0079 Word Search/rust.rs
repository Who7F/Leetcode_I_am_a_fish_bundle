impl Solution {
    fn findWord(board: &mut Vec<Vec<char>>, word: &str, i: usize, j: usize, mut index: usize) -> bool {
        if board[i][j] != word.chars().nth(index).unwrap() {
            return false;
        }

        index += 1;

        if index == word.len(){
            return true;
        }

        let temp = board[i][j];
        board[i][j] = '-';
        let directions = [(0, 1),(1, 0),(0, usize::MAX),(usize::MAX, 0)];

        for &(dx, dy) in &directions {
            let new_i = i.wrapping_add(dx);
            let new_j = j.wrapping_add(dy);
            if new_i < board.len() && new_j < board[0].len() {   
                if Self::findWord(board, word, new_i, new_j, index) {
                    return true;
                }
            }
        }

        board[i][j] = temp;
        false
    }

    pub fn exist(mut board: Vec<Vec<char>>, word: String) -> bool {
        for i in 0..board.len(){
            for j in 0..board[0].len(){
                if Self::findWord(&mut board, &word, i, j, 0) {
                    return true;
                }
            }
        }
        false
    }
}


