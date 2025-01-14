impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut anc = vec![vec![]];
        
        for num in nums {
            let l = anc.len();
            for i in 0..l {
                let mut temp = anc[i].clone();
                temp.push(num);
                anc.push(temp)
            }
        }
        anc
    }
}