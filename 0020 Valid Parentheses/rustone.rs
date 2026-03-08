use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut hash_m = HashMap::new();
        hash_m.insert('{', '}');
        hash_m.insert('[', ']');
        hash_m.insert('(', ')');
        let mut stack = Vec::new(); 
        
        for c in s.chars() {
            if let Some(&closing_b) = hash_m.get(&c) {
                stack.push(closing_b);
            }
            else if stack.pop() != Some(c) {
                return false;
            }
        }
        stack.is_empty()
    }
}