impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        if num == 1{
            return true
        }
        use std::cmp::Ordering;
        let mut n = num;
        let mut lit = 0;
        while lit < n{
            let cnt = lit + (n - lit) / 2;
            match cnt.checked_mul(cnt) {
                Some(square) => match square.cmp(&num){
                    Ordering::Equal => return true,
                    Ordering::Less => lit = cnt + 1,
                    Ordering::Greater => n = cnt,
                },
                None => n = cnt,
            }
        }
        false
    }
}