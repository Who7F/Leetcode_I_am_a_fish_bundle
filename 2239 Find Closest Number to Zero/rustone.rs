impl Solution {
    pub fn find_closest_number(nums: Vec<i32>) -> i32 {
        let mut anc = nums[0];
        for i in nums.iter() {
            if i.abs() < anc.abs(){
                anc = *i;
            }else if i.abs() == anc.abs(){
                anc = std::cmp::max(anc, *i);
            }
        }
        anc
    }
}