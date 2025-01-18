// recursive
// Gets all the possible permutations

impl Solution {
    fn findPermuta(nums: &mut Vec<i32>, res: &mut Vec<Vec<i32>>, index: usize){
        if index == nums.len() {
            res.push(nums.clone());
        }else{
            for i in index..nums.len(){
                nums.swap(i, index);
                Self::findPermuta(nums, res, index + 1);
                nums.swap(i, index);                
            }
        }
    }
    
    pub fn permute(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        // Start the recursive process
        Self::findPermuta(&mut nums, &mut res, 0);
        res
    }
}