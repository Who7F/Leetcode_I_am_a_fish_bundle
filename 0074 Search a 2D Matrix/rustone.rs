impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {

        let (m, n) = (matrix.len(), matrix[0].len());
        let (mut lit, mut big) = (0 as isize, (m * n - 1) as isize);
        use std::cmp::Ordering;
        while lit <= big{
            let mid = lit + (big - lit) / 2;
            let mid_val = matrix[mid as usize/n][mid as usize%n];
            match mid_val.cmp(&target){
                Ordering::Equal => return true,
                Ordering::Less => lit = mid + 1,
                Ordering::Greater => big = mid - 1,
            }
        }
        false
    }
}