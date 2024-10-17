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

// struct Solution {
//    max_diameter: i32
// }
// There is an unseen struct Solution on line 64

impl Solution {
    
    fn hight_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>, max_diameter: &mut i32) -> i32 {
        match root{
            None => 0,
            Some(node) =>{
                let left_branch = Self::hight_of_binary_tree(node.borrow().left.clone(), max_diameter);
                let right_branch = Self::hight_of_binary_tree(node.borrow().right.clone(), max_diameter);

                // self.max_diameter = self.max_diameter.max(left_branch + right_branch);
                *max_diameter = (*max_diameter).max(left_branch + right_branch);
                
                left_branch.max(right_branch) + 1
            }
        }
    }
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        // self.max_diameter = 0;
        let mut max_diameter = 0;
        Self::hight_of_binary_tree(root, &mut max_diameter);
        // self.max_diameter 
        max_diameter       
    }
}