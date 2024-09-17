impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut anc = String::with_capacity(word1.len() + word2.len());
        let min_len = std::cmp::min(word1.len(),word2.len());

        for i in 0..min_len{
            anc.push(word1.chars().nth(i).unwrap());
            anc.push(word2.chars().nth(i).unwrap());
        }

        anc.push_str(&word1[min_len..]);
        anc.push_str(&word2[min_len..]);

        anc
    }
}