class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        if(source == destination) {
            return true;
        }

        unordered_map<int, vector<int>> gph;
        for(const auto& edge : edges) {
            gph[edge[0]].push_back(edge[1]);
            gph[edge[1]].push_back(edge[0]);
        }
        unordered_set<int> seen;
        vector<int> stack;

        seen.insert(source);
        stack.push_back(source);

        while(not stack.empty()){
            int node = stack.back();
            stack.pop_back();
            if (node == destination) {
                return true;
            }
            for(int n_node : gph[node]) {
                if (seen.find(n_node) == seen.end()) {
                    seen.insert(n_node);
                    stack.push_back(n_node);
                }
            }
        }
        return false;
    }
};