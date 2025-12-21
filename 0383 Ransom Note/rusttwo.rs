use std::collections::HashMap;

impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut seen = HashMap::new();

        magazine.chars().for_each(|c| {
            *seen.entry(c).or_insert(0) += 1;
        });

        ransom_note.chars().all(|c| {
            let count = seen.entry(c).or_insert(0);
            *count -= 1;
            *count >= 0
        }) 
    }
}