class Solution {
private:
    vector<int> state;
    vector<vector<int>> graph;
    vector<int> myList;

    bool dfs(int node){
        if (state[node] == 2) return true;
        if (state[node] == 1) return false;

        state[node] = 1;

        for (auto g : graph[node]){
            if (!dfs(g)) return false;
        }
        state[node] = 2;
        myList.push_back(node);
        return true;
    }
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        myList.clear();
        graph.assign(numCourses, {});
        state.assign(numCourses, 0);

        for (auto p : prerequisites){
            graph[p[1]].push_back(p[0]);
        }

        for (int i = 0; i < numCourses; i++){
            if (!dfs(i)) return {};
        }
        
        reverse(myList.begin(), myList.end());
        return myList;
    }
};