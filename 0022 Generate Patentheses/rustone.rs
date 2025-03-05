impl Solution {
    fn getPairs(res: &mut Vec<String>, sol: String, left: usize, right: usize) {
        if left + right == 0 {
            res.push(sol.clone())
        }

        if left > 0 {
            Self::getPairs(res, format!("{}(", sol), left - 1, right + 1);
        }

        if right > 0 {
            Self::getPairs(res, format!("{})", sol), left, right - 1);
        }
    }

    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut res = Vec::new();
        Self::getPairs(&mut res, String::new(), n as usize, 0);
        res
    }
}