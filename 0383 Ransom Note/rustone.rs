use std::collections::HashMap;

impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut seen = HashMap::new();

        for c in magazine.chars() {
            *seen.entry(c).or_insert(0) += 1;
        }

        for c in ransom_note.chars() {
            let count = seen.entry(c).or_insert(0);
            *count -= 1;
            if *count < 0 {
                return false;
            }
        }

        true
    }
}