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
    fn is_valid(node: Option<Rc<RefCell<TreeNode>>>, lit: i64, big: i64) -> bool {
        match node {
            None => true,
            Some(n) => {
                let node_ref = n.borrow();
                node_ref.val as i64 > lit 
                    && (node_ref.val as i64) < big
                    && Self::is_valid(node_ref.left.clone(), lit, node_ref.val as i64)
                    && Self::is_valid(node_ref.right.clone(), node_ref.val as i64, big)
            }
        }
    }
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::is_valid(root, i64::MIN, i64::MAX)
    }
}