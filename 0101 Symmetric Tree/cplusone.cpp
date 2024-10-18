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
public:
    bool isMirror(TreeNode* leftBranch, TreeNode* rightBranch){
        if(!leftBranch && !rightBranch){
            return true;
        }
        if(!leftBranch || !rightBranch){
            return false;
        }
        bool mirror = isMirror(leftBranch->left, rightBranch->right) && isMirror(leftBranch->right, rightBranch->left);

        return leftBranch->val == rightBranch->val && mirror;
    }

    bool isSymmetric(TreeNode* root) {
        return isMirror(root->left, root->right);
    }
};