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
use std::collections::VecDeque;
impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        if let Some(r) = root {
            let mut anc = Vec::new();
            let mut queue = VecDeque::new();
            queue.push_back(r);

            while !queue.is_empty() {
                let mut level = Vec::new();
                for _ in 0..queue.len() {

                    let node = queue.pop_front().unwrap();
                    let node_ref = node.borrow();

                    level.push(node_ref.val);

                    if let Some(left) = node_ref.left.clone() {
                        queue.push_back(left);
                    }
                    if let Some(right) = node_ref.right.clone() {
                        queue.push_back(right);
                    }
                }
                anc.push(level);
            }
            return anc
        }
        vec![]
    }
}