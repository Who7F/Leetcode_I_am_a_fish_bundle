impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        nums.chunk_by(|&a, &b| (a + 1) == b)
            .map(|chunk| (chunk[0], chunk[chunk.len() - 1])) // get head and tail
            .map(|(head, tail)| {
                if head == tail {
                    head.to_string()
                } else {
                    format!("{}->{}", head, tail)
                }
            })
            .collect()
    }
}