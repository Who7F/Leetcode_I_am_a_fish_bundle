impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let l = matrix.len();
        for i in 0..l{
            for j in 0..i{
                (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j]);
            }
        }
        for i in 0..l/2{
            for j in 0..l{
                (matrix[j][i], matrix[j][l - i - 1]) = (matrix[j][l - i - 1], matrix[j][i]);
            }
        }
    }
}