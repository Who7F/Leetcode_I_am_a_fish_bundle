impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut anc: Vec<i32> = vec![0; temperatures.len()];
        let mut stack = Vec::new();
        for i in 0..temperatures.len() {
            while !stack.is_empty() && temperatures[i] > temperatures[*stack.last().unwrap()] {
                let idx = stack.pop().unwrap();
                anc[idx] = (i - idx) as i32; 
            }
            stack.push(i);
        }
        anc
    }
}