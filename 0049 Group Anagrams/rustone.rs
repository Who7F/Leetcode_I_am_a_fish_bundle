use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let map = strs
            .into_iter()
            .fold(HashMap::<String, Vec<String>>::new(), |mut acc, s| {
                let mut chars: Vec<char> = s.chars().collect();
                chars.sort_unstable();

                let key: String = chars.into_iter().collect();
                acc.entry(key).or_default().push(s);
                acc
            });

        map.into_values().collect()
    }
}
