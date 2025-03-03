impl Solution {
    fn getCobinations(
        digits: &str, 
        res: &mut Vec<String>, 
        index: usize, 
        sol: String, 
        letter_map: &std::collections::HashMap<char, &str>) {
        
        if index == digits.len() {
            res.push(sol.clone())
            
        } else { 
            if let Some(letters) = letter_map.get(&digits.chars().nth(index).unwrap()) {
                
                for c in letters.chars() {
                    Self::getCobinations(digits, res, index + 1, format!("{}{}", sol, c), letter_map)
                }
            }        
        }
    }

    pub fn letter_combinations(digits: String) -> Vec<String> {
        let mut res = Vec::new();

        if digits.is_empty() {
            return res
        }

        let letter_map: std::collections::HashMap<char, &str> = [
            ('2', "abc"),  ('3', "def"), ('4', "ghi"), ('5', "jkl"), 
            ('6', "mno"), ('7', "pqrs"), ('8', "tuv"), ('9', "wxyz")
            ].iter().cloned().collect();

        Self::getCobinations(&digits, &mut res, 0, String::new(), &letter_map);
        res
    }
}