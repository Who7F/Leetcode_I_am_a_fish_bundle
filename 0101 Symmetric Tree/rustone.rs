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
    fn is_mirror(left: Option<Rc<RefCell<TreeNode>>>, right: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match(left, right) {
            (None, None) => true,
            (Some(left), Some(right)) =>{
                let left_ref = left.borrow();
                let right_ref = right.borrow();
                if left_ref.val != right_ref.val {
                    return false
                }
                return Self::is_mirror(left_ref.left.clone(), right_ref.right.clone()) && 
                    Self::is_mirror(left_ref.right.clone(), right_ref.left.clone())
            },
            _ => false,
        }
    }

    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match root {
            Some(node) => {
                let node_ref = node.borrow();
                return Self::is_mirror(node_ref.left.clone(), node_ref.right.clone())
            },
            None => true,
        }
    }
}