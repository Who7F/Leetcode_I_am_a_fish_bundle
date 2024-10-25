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
    bool isClonetree(TreeNode* root, TreeNode* subRoot) {
        if(!root && !subRoot) {
            return true;
        }
        if(!root || !subRoot) {
            return false;
        }
        
        return root->val == subRoot->val && isClonetree(root->left, subRoot->left) && isClonetree(root->right, subRoot->right);
    }

public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(!subRoot) {
            return true;
        }
        if(!root) {
            return false;
        }
        if(isClonetree(root, subRoot)) {
            return true;
        }
        return isSubtree(root->left, subRoot) or isSubtree(root->right, subRoot);
    }
};
