class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        if (n == 0) return 0;

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        vector<bool> seen(n, false);
        int cost = 0;

        heap.push({0, 0});


        while (!heap.empty()) {
            auto [nodeCost, node] = heap.top();
            heap.pop();
            if (seen[node]) continue;

            seen[node] = true;
            cost += nodeCost;

            for (int nei = 0; nei < n; nei++) {
                if (!seen[nei]) {
                    int nextCost = (abs(points[node][0] - points[nei][0]) + abs(points[node][1] - points[nei][1]));
                    heap.push({nextCost, nei});
                }
            }
        }
    return cost;
    }
};