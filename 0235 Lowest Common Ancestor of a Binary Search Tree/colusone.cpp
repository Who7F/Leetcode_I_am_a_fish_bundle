/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
private:
    TreeNode* CommonAncestor(TreeNode* node, int p, int q) {
        if(!node) {
            return node;
        }

        if(node->val > q && node->val > p) {
            return CommonAncestor(node->left, p, q);
        }

        if(node->val < q && node->val < p) {
            return CommonAncestor(node->right, p, q);
        }

        return node;
    }

public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return CommonAncestor(root,  p->val,  q->val);
    }
};

