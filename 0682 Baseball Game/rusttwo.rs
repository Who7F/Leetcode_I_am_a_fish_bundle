impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        operations
        .into_iter()
        .fold(Vec::<i32>::new(), |mut stack, op| {
            match op.as_str() {
                "+" => {
                    let n = stack.len();
                    stack.push(stack[n - 1] + stack[n - 2]);
                }
                "D" => {
                    stack.push(2 * stack[stack.len() - 1]);
                }
                "C" => {
                    stack.pop();
                }
                _ => {
                    stack.push(op.parse().unwrap());
                }
            }
            stack
        })
        .iter()
        .sum()
    }
}