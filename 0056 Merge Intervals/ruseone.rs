impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        intervals.sort_by_key(|v| v[0]);

        let mut anc: Vec<Vec<i32>> = Vec::new();
        anc.push(intervals[0].clone());

        for i in intervals.into_iter().skip(1) {
            let last = anc.last_mut().unwrap();
            if last[1] >= i[0] {
                last[1] = last[1].max(i[1]);
            } else {
                anc.push(i);
            }
        }
        anc
    }
}