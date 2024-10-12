// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn check_balance(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if let Some(node) = root{
            let node_ref = node.borrow();

            let left_depth = Self::check_balance(node_ref.left.clone());
            if left_depth == -1{
                return -1
            }

            let right_depth = Self::check_balance(node_ref.right.clone());
            if right_depth == -1{
                return -1
            }

            if (left_depth - right_depth).abs() > 1{
                return -1
            }

            return 1 + left_depth.max(right_depth)
        }
        0
    }
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::check_balance(root.clone()) != -1
    }
}