/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(!head)
            return nullptr;
        
        unordered_map<Node*, Node*> nodeMap;
        Node* h = head;
        
        while(h){
            nodeMap[h] = new Node(h-> val);
            h = h->next;
        }

        h = head;

        while(h){
            nodeMap[h]->next = nodeMap[h->next];
            nodeMap[h]->random = nodeMap[h->random];
            h = h->next;
        }

        return nodeMap[head];
    }