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
    fn common_ancestor(node: Option<Rc<RefCell<TreeNode>>>, p: i32, q: i32) -> Option<Rc<RefCell<TreeNode>>> {
        match node {
            Some(node_rc) =>{
                let node_ref = node_rc.borrow();
                if node_ref.val > q && node_ref.val > p {
                    Self::common_ancestor(node_ref.left.clone(), p, q)
                }
                else if node_ref.val < q && node_ref.val < p {
                    Self::common_ancestor(node_ref.right.clone(), p, q)
                } else{
                    Some(Rc::clone(&node_rc))
                }
                
            }
            None => None,
        }
    }

    pub fn lowest_common_ancestor(root: Option<Rc<RefCell<TreeNode>>>, p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let (Some(q_rc), Some(p_rc)) = (q, p) {
            let (q_val, p_val) = (q_rc.borrow().val, p_rc.borrow().val);
            Self::common_ancestor(root, q_val, p_val)
        } else{
            None
        }
        
    }
}