class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        unordered_map<int, vector<pair<int, int>>> graph;
        for (auto &t : times) {
            graph[t[0]].push_back({t[2], t[1]});
        }

        unordered_map<int, int> seen;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;

        heap.push({0, k});

        while (!heap.empty()) {
            auto [time, node] = heap.top();
            heap.pop();
            
            if (seen.contains(node)) continue;

            seen[node] = time;

            for (auto &g : graph[node]) {
                if (!seen.contains(g.second)) {
                    heap.push({time + g.first, g.second});
                }   
            }
        }
        if (seen.size() == n) {
            int maxTime;
            for (auto &[node, t] : seen) {
                maxTime = max(maxTime, t);
            }
            return maxTime;
        }
        return -1;
    }
};