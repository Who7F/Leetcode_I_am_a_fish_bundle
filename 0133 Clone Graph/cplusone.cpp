/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;

        unordered_map<Node*, Node*> seen;
        queue<Node*> que;

        seen[node] = new Node(node -> val);

        que.push(node);

        while(!que.empty()) {
            Node* curr = que.front();
            que.pop();

            for (Node* n : curr -> neighbors) {
                if (seen.find(n) == seen.end()) {
                    seen[n] = new Node(n -> val);
                    que.push(n);
                }
                seen[curr] -> neighbors.push_back(seen[n]);
            }
        }
        return seen[node];
    }
};