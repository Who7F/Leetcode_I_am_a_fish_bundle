impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let (mut prev2, mut prev1) = (cost[0], cost[1]);

        for c in &cost[2..] {
            let cur = c + prev1.min(prev2);
            prev2 = prev1;
            prev1 = cur;
        }
        prev1.min(prev2)
    }
}