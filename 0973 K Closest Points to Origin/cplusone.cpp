class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        using maxHeap = priority_queue<pair<int, vector<int>>, vector<pair<int, vector<int>>>, less<>>;
        maxHeap heap;

        for(auto& p : points){
            int destance = p[0] * p[0] + p[1] * p[1];
            heap.push({destance, p});

            if (heap.size() > k){
                heap.pop();
            }       
        }
        vector<vector<int>> anc;
        while (!heap.empty()) {
            anc.push_back(heap.top().second);
            heap.pop();
        }
        return anc;
    }
};