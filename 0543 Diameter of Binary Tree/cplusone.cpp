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
    int maxDiemeter = 0;

    int hightOfBinaryTree(TreeNode* root) {
        if(root == nullptr){
            return 0;
        }
        int leftBranch = hightOfBinaryTree(root->left);
        int rightBranch = hightOfBinaryTree(root->right);

        maxDiemeter = max(maxDiemeter, leftBranch + rightBranch);

        return max(leftBranch, rightBranch) + 1;
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if(root == nullptr){
            return 0;
        }
        hightOfBinaryTree(root);

        return maxDiemeter;
    }
};