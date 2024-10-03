impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut anc: i32  = 0;
        let mut count = vec![0; 128];
        let mut l = 0;
        let s_chars: Vec<char> = s.chars().collect();
        for i in 0..s_chars.len(){
            count[s_chars[i] as usize] += 1;
            while count[s_chars[i] as usize] > 1{
                count[s_chars[l] as usize] -= 1;
                l += 1;
            }
            anc = anc.max((i - l + 1) as i32);
        }
        
        anc
    }
}