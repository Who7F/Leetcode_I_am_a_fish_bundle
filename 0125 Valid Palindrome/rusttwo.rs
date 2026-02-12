impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let f: Vec<char> = s
            .chars()
            .filter(|c| c.is_alphanumeric())
            .map(|c| c.to_ascii_lowercase())
            .collect();
            
        f.iter().eq(f.iter().rev())
    }
}