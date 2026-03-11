impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        for c in tokens{
            if let Ok(num) = c.parse::<i32>() {
                stack.push(num);
            } else {
                let top = stack.pop().unwrap();
                let bot = stack.pop().unwrap();
                let res = match c.as_str(){
                    "+" => bot + top,
                    "-" => bot - top,
                    "*" => bot * top,
                    "/" => bot / top,
                    _ => unreachable!(),
                };
            stack.push(res);
            }
            
        }
        stack.pop().unwrap()
    }
}