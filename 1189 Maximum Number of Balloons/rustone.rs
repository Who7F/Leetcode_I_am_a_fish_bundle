impl Solution {
    pub fn max_number_of_balloons(text: String) -> i32 {
        let mut freq = std::collections::HashMap::new();
        let mut need = std::collections::HashMap::new();

        text.chars().for_each(|c| *freq.entry(c).or_insert(0) += 1);
        "balloon".chars().for_each(|c| *need.entry(c).or_insert(0) += 1);
        
        need.iter().map(|(&c, &cnt)| freq.get(&c).unwrap_or(&0) / cnt).min().unwrap_or(0)
    }
}