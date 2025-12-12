impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let l = nums.len();
        let mut anc = vec![1; l];

        let mut total = 1;

        for i in 1..l {
            total = total * nums[i - 1];
            anc[i] = anc[i] * total;
        }

        total = 1;

        for i in (1..l).rev() {
            total = total * nums[i];
            anc[i - 1] = anc[i - 1] * total;
        }

        anc
    }
}