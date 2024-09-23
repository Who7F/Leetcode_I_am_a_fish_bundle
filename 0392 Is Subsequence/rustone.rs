impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let (mut i, mut j) = (0, 0);
        let (s1, t1) = (s.as_bytes(), t.as_bytes());
        while i < s1.len() && j < t1.len(){
            if s1[i] == t1[j]{
                i += 1;
            }
            j += 1;
        }
        i == s1.len()    
    }
    
}