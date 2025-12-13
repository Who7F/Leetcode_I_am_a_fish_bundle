class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> anc;
        anc.push_back(intervals[0]);

        int n = 0;
        for (auto &i : intervals) {
            if (anc[n][1] >= i[0]) {
                if (anc[n][1] < i[1]) {
                    anc[n][1] = i[1];
                }
            } else {
                anc.push_back(i);
                n++;
            }

        }
        return anc;
    }
};