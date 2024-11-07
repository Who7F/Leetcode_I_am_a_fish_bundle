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
    fn in_order(root: Option<Rc<RefCell<TreeNode>>>, prev: i32) -> (i32, i32){
        if let Some(node) = root {
            let node_ref = node.borrow();
            let mut anc = i32::MAX;
            
            let (left_anc, left_prev) = Self::in_order(node_ref.left.clone(), prev);
            anc = left_anc;

            if left_prev != -1 {
                anc = anc.min(node_ref.val - left_prev);
            }


            let (right_anc, right_prev) = Self::in_order(node_ref.right.clone(), node_ref.val);

            (anc.min(right_anc), right_prev)
        } else {
            (i32::MAX, prev)
        }

    }

    pub fn get_minimum_difference(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let (anc, _) = Self::in_order(root, -1);
        anc
    }
}