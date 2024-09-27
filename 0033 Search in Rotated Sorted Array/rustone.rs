impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let(mut lit, mut big) = (0 as isize, (nums.len() - 1) as isize);
        while lit <= big{
            let mid = lit + (big - lit) / 2;
            
            if nums[mid as usize] == target{
                return mid as i32;
            }
            if nums[lit as usize] <= nums[mid as usize]{
                if nums[lit as usize] <= target && target < nums[mid as usize]{
                    big = mid - 1;
                }else{
                    lit = mid + 1;
                }
            }else{
                if nums[mid as usize] < target && target <= nums[big as usize]{
                    lit = mid + 1;
                }else{
                    big = mid - 1;
                }
            }
        }

        -1
    }
}