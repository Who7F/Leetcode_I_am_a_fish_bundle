impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut vec: Vec<i32> = Vec::new();
        for i in operations {    
            match i.as_str(){
                "+" => {
                    vec.push(vec[vec.len() - 1] + vec[vec.len() - 2]);
                }
                "D" => {
                    vec.push(2* vec[vec.len() - 1]);
                }
                "C" => {
                    vec.pop();
                }
                _ => {
                   vec.push(i.parse().unwrap());
                }
            }
        }
        vec.iter().sum()
    }
}