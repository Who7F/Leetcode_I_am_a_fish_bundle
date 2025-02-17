// Pointer-based design,
// recursive
// Finds base sebset
impl Solution {
    fn fundNumber(n: i32, k: usize, res: &mut Vec<Vec<i32>>, sol: &mut Vec<i32>) {
        if sol.len() == k{
            // Adds base case (current subset to results)
            res.push(sol.clone());
        }else{
            // Left branch (exclude current element)
            if n > (k - sol.len()) as i32{
                Self::fundNumber(n - 1, k, res, sol);
            }
            // Right branch (include current element)
            sol.push(n);
            Self::fundNumber(n - 1, k, res, sol);
            sol.pop();
        }
    }

    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        let mut sol = Vec::new();
        Self::fundNumber(n, k as usize, &mut res, &mut sol);
        res
    }
}