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
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode bigDaddyD(0, head);
        ListNode* blindAl = &bigDaddyD;
        
        for(int i = 0; i < n; i++)
            head = head->next;

        while(head != nullptr){
            head = head->next;
            blindAl = blindAl->next;
        }

        blindAl->next = blindAl->next->next;
        
        return bigDaddyD.next;
    }
};