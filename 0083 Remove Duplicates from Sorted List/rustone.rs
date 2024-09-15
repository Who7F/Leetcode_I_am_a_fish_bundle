impl Solution {
    pub fn delete_duplicates(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {

        let mut current = head.as_mut();  

        while let Some(node) = current {
            while let Some(next_node) = node.next.as_mut() {
                if node.val == next_node.val {
                    node.next = next_node.next.take();
                } else {
                    break;
                }
            }
            current = node.next.as_mut();
        }

        head
    }
}