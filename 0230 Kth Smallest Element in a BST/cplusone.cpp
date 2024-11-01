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
    int kth;
    int anc;

    void getKth(TreeNode* root) {
        if(!root) {
            return;
        }
        getKth(root->left);
        kth--;
        if(kth == 0) {
            anc = root->val;
        } else if (kth > 0) {
            getKth(root->right);
        }
        return;
    }

public:
    int kthSmallest(TreeNode* root, int k) {
        kth = k;
        getKth(root);
        return anc;
    }
};