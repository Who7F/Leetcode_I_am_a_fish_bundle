impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let (mut low, mut max_cnt) = (0, 0);
        let mut count = vec![0; 128];
        let s_byte: Vec<u8> = s.bytes().collect();
        for i in 0..s_byte.len(){
            count[s_byte[i] as usize] += 1;
            max_cnt = max_cnt.max(count[s_byte[i] as usize]);

            if 1 + i - low - max_cnt > k as usize{
                count[s_byte[low] as usize] -= 1;
                low += 1;
            } 
        }
        (s.len() - low) as i32
    }
}