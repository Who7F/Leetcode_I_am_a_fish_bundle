impl Solution {
    fn check_vals(
        numbers: &[i32],
        target: i32,
        left: usize,
        right: usize,
    ) -> Vec<i32> {
        if left >= right {
            return vec![-1, -1];
        }

        let temp = numbers[left] + numbers[right];

        match temp.cmp(&target) {
            Ordering::Less => Self::check_vals(numbers, target, left + 1, right),
            Ordering::Greater => Self::check_vals(numbers, target, left, right - 1),
            Ordering::Equal => vec![(left + 1) as i32, (right + 1) as i32],
        }
    }

    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        Self::check_vals(&numbers, target, 0, numbers.len() - 1)
    }
}