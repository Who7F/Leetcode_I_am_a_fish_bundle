// The API isBadVersion is defined for you.
// isBadVersion(version:i32)-> bool;
// to call it use self.isBadVersion(version)

impl Solution {
    pub fn first_bad_version(&self, mut n: i32) -> i32 {
		let mut lit = 0;
        while lit < n{
            let anc = lit + (n - lit) / 2;
            match self.isBadVersion(anc){
                true => n = anc,
                false => lit = anc + 1,
            }
        }
        n 
    }
}