impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let (mut low, mut hight) = (prices[0], 0);
        let mut anc = 0;
        for price in prices{
            if price > hight{
                hight = price;
                if hight - low > anc{
                    anc = hight - low;
                }
            }
            if price < low{
                low = price;
                hight = price;
            }
        }
        anc
    }
}