/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    int anc = 1e5;
    optional<int> prev;
    
    void in_order(TreeNode* node){
        if(!node) {
            return;
        }

        in_order(node->left);

        if(prev.has_value()){
            anc = min(anc, node->val - prev.value());
        }
            
        prev = node->val;
            
        in_order(node->right);
    }

public:
    int getMinimumDifference(TreeNode* root) {
        in_order(root);
        return anc;
    }
};