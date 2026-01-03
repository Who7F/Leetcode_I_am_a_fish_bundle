use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        
        let mut seen = HashMap::new();

        s.chars().for_each(|c| *seen.entry(c).or_insert(0) += 1);
        t.chars().for_each(|c| *seen.entry(c).or_insert(0) -= 1);

        seen.into_values().all(|v| v == 0)
    }
}