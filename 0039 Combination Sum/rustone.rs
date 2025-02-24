impl Solution {
    fn getSum(res: &mut Vec<Vec<i32>>, sol: &mut Vec<i32>, candidates: &Vec<i32>, target: i32, index: usize, l: i32) {
        if l == target {
            res.push(sol.clone())
        }

        if l > target {
            return
        }

        for i in index..candidates.len() {
            sol.push(candidates[i]);
            Self::getSum(res, sol, candidates, target, i, l + candidates[i]);
            sol.pop();
        }
    }

    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        let mut sol = Vec::new();
        Self::getSum(&mut res, &mut sol, &candidates, target, 0, 0);
        res
    }
}