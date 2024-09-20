impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let mut lit = 0;
        let mut big = nums.len() as i32 - 1;

        while lit <= big{
            let anc = lit + (big - lit) / 2;
            let num = nums[anc as usize];
            if target > num{
                lit = anc + 1;
            }else if target < num{
                big = anc - 1;
            }else{
                return anc;
            }
        }
        lit        
    }
}