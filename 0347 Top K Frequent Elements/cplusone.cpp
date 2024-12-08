class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqMap;
        using minPair = pair<int, int>;
        priority_queue<minPair, vector<minPair>, greater<minPair>> minHeap;
        for(int n: nums){
            freqMap[n]++;
        }
        for(auto& [n, f]: freqMap){
            if (minHeap.size() < k) {
                minHeap.push({f, n});
            } else if (f > minHeap.top().first) {
                minHeap.push({f,n});
                minHeap.pop();
            }
        }
        vector<int> res;
        while(!minHeap.empty()){
            res.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return res;
    }
};