impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n < 2 {
            return n;
        }

        let (mut a, mut b) = (0, 1);

        for _ in 0..n {
            (a, b) = (b, a + b);
        }

        b
    }
}