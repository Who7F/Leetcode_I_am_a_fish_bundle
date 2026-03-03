impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let (mut lo, mut hi) = (0, height.len() - 1);
        let mut cnt = 0;
        let mut m = 0;
        while lo < hi{
            match height[lo] < height[hi]{
                true  if height[lo] > m => {m = height[lo]; lo += 1;}
                true                     => {cnt += m - height[lo]; lo += 1;}
                false if height[hi] > m => {m = height[hi]; hi -= 1;}
                false                    => {cnt += m - height[hi]; hi -= 1;} 
            }
        }

        cnt
    }
}