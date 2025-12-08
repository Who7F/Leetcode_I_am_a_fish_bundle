impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        strs.into_iter()
            .reduce(|a, b| {
                a.chars()
                    .zip(b.chars())
                    .take_while(|(x, y)| x == y)
                    .map(|(c, _)| c)
                    .collect()
            })
            .unwrap_or_default()
    }
}
