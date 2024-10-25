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
    fn is_clone_tree(root: Option<Rc<RefCell<TreeNode>>>, sub_root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match(root, sub_root) {
            (None, None) => true,
            (Some(root), Some(sub_root)) =>{
                let root_ref = root.borrow();
                let sub_ref = sub_root.borrow();
                root_ref.val == sub_ref.val 
                    && Self::is_clone_tree(root_ref.left.clone(), sub_ref.left.clone()) 
                    && Self::is_clone_tree(root_ref.right.clone(), sub_ref.right.clone()) 
            },
            _ => false
        }
    }

    pub fn is_subtree(root: Option<Rc<RefCell<TreeNode>>>, sub_root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        if sub_root.is_none() {
            return true
        }
        if let Some(root_node) = root {
            let root_ref = root_node.borrow();
        
            if Self::is_clone_tree(Some(root_node.clone()), sub_root.clone()) {
                return true
            }
            Self::is_subtree(root_ref.left.clone(), sub_root.clone()) || Self::is_subtree(root_ref.right.clone(), sub_root)
        } else {
            false
        }
    }
}

