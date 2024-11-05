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
    fn get_kth(root: Option<Rc<RefCell<TreeNode>>>, k: &mut i32) -> Option<i32> {
        if let Some(node) = root {
            let node_ref = node.borrow();

            if let Some(val) = Self::get_kth(node_ref.left.clone(), k) {
                return Some(val)
            }
            *k -= 1;
            if *k == 0 {
                return Some(node_ref.val)
            } 
            return Self::get_kth(node_ref.right.clone(), k)
        }
        None
    }

    pub fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, mut k: i32) -> i32 {
        Self::get_kth(root, &mut k).unwrap_or(-1)
    }
}