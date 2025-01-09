// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
use std::cmp::Ordering;
use std::collections::BinaryHeap;

impl PartialOrd<ListNode> for ListNode{
    fn partial_cmp(&self, other: &ListNode) -> Option<Ordering>{
        other.val.partial_cmp(&self.val)
        //self.val.partial_cmp(&other.val)
    }
}
impl Ord for ListNode{
    fn cmp(&self, other: &Self) -> Ordering{
        other.val.cmp(&self.val)
        //self.val.cmp(&other.va;)
    }
}

impl Solution {
    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        let mut heap: BinaryHeap<Box<ListNode>> = BinaryHeap::with_capacity(lists.len());

        for list in lists.into_iter() {
            if let Some(node) = list {
                heap.push(node);
            }
        }

        let mut dummy = Box::new(ListNode::new(0));
        let mut current = &mut dummy;

        while let Some(mut node) = heap.pop() {

            current.next = Some(node.clone());
            current = current.next.as_mut().unwrap();

            if let Some(next_node) = node.next.take() {
                heap.push(next_node);
            }
        }

        dummy.next
    }
}