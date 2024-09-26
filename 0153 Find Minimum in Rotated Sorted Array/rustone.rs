impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let (mut lit, mut big) = (0, nums.len() - 1);  
        //no type type gymnastics as is lit < big and not <=
        //This mean we stick with unsigned ints
        while lit < big{ 
            let mid = lit + (big - lit) / 2;
            if nums[mid] > nums[big]{
                lit = mid + 1;
            }else{
                big = mid;
            }
        }
        nums[lit]
        
    }
}