impl Solution {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        stones.chars().filter(|c| jewels.contains(*c)).count() as i32
    }
}