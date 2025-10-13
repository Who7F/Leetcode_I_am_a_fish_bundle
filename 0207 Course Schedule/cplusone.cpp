class Solution {
private:
    vector<int> states;
    vector<vector<int>> graph;

    bool dfs(int node) {
        if(states[node] == 2){
            return true;
        }
        else if(states[node] == 1){
            return false;
        }
        states[node] = 1;

        for(auto n : graph[node]){
            if(!dfs(n)){
                return false;
            }
        }

        states[node] = 2;

        return true;
    }

public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {

        graph.assign(numCourses, {});
        states.assign(numCourses, 0);

        for(auto &x : prerequisites) {
            int a = x[0], b = x[1];
            graph[b].push_back(a);
        }
        

        for(int i = 0; i < numCourses; i++){
            if(!dfs(i)){
                return false;
            }
        }
        return true;
    }
};

