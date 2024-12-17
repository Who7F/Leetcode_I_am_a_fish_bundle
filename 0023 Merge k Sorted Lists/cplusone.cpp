/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
struct Triplet{
    int val; 
    int idx;
    ListNode* node; 

    bool operator>(const Triplet& other) const {
        return val > other.val;
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        using minHeap = priority_queue<Triplet, vector<Triplet>, greater<Triplet>>;
        minHeap heap;

        for(int i = 0; i < lists.size(); i++) {
            if (lists[i]) {
                heap.push({lists[i]->val, i, lists[i]});
            }
        }

        ListNode dummy(0);
        ListNode* current = &dummy;
        while (!heap.empty()) {
            Triplet t = heap.top();
            heap.pop();
            current->next = t.node;
            current = current->next;

            if (t.node->next){
                heap.push({t.node->next->val, t.idx, t.node->next});
            }
        }
        return dummy.next;
    }
};