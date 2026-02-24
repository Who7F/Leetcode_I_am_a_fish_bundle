impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort();
        let mut res: Vec<Vec<i32>> = Vec::new();
        let n = nums.len();

        for i in 0..n.saturating_sub(2) {
            if nums[i] > 0 {
                break;
            }

            if i > 0 && nums[i] == nums[i - 1] {
                continue;
            }

            let mut left = i + 1;
            let mut right = n - 1;

            while left < right {
                let temp = nums[i] + nums[left] + nums[right];

                if temp == 0 {
                    res.push(vec![nums[i], nums[left], nums[right]]);

                    left += 1;
                    right -= 1;

                    while left < right && nums[left] == nums[left - 1] {
                        left += 1;
                    }

                    while left < right && nums[right] == nums[right + 1] {
                        right -= 1;
                    }
                } else if temp < 0 {
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }
        res
    }
}