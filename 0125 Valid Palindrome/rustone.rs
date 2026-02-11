impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let c: Vec<char> = s.chars().collect();

        if c.is_empty() {
            return true;
        }

        let mut left = 0;
        let mut right = c.len() - 1;

        while left < right {
            if !c[left].is_alphanumeric() {
                left += 1;
            } else if !c[right].is_alphanumeric() {
                right -= 1;
            } else if c[left].to_ascii_lowercase() != c[right].to_ascii_lowercase() {
                return false;
            } else {
                left += 1;
                right -= 1;
            }
        }

        true
    }
}