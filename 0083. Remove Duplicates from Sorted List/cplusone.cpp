class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == NULL)
            return head;
        
        ListNode* h = head;
        while (h->next){
            if(h->val == h->next->val)
                h->next = h->next->next;
            else
                h = h->next;
        }
        return head;
    }
};