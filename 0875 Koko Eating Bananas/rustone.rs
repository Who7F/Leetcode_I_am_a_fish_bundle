impl Solution {
    fn eats_bananers(piles: &Vec<i32>, h: i32, bits: i32) -> bool {
        let mut n = 0;
        for &p in piles{
            n += ((p as f64)/ (bits as f64)).ceil() as i32;
        }
        n <= h
    }
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let (mut lit, mut big) = (1, *piles.iter().max().unwrap());
        while lit < big{
            let bite = lit + (big - lit) / 2;
            match Self::eats_bananers(&piles, h, bite){
                true => big = bite,
                false => lit = bite + 1,
            }
        }
        lit    
    }
}