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
    pub fn has_path_sum(root: Option<Rc<RefCell<TreeNode>>>, mut target_sum: i32) -> bool {
        if let Some(node) = root {
            let node_ref = node.borrow();
            if node_ref.left.is_none() && node_ref.right.is_none() && node_ref.val == target_sum {
                return true
            }
            target_sum -= node_ref.val;

            return Self::has_path_sum(node_ref.left.clone(), target_sum) || Self::has_path_sum(node_ref.right.clone(), target_sum)
        }
        false
    }
}