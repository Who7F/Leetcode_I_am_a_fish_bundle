impl Solution {
    pub fn remove_nth_from_end(mut head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut node = head.clone();
        let mut blindAl = &mut head;
        
        for _ in 0..n{
            node = node.map(|n| n.next)?;
        }

        while let Some(n) = node{
            node = n.next;
            blindAl = &mut blindAl.as_mut()?.next;
        }

        *blindAl = blindAl.as_mut().and_then(|n| n.next.take());

        head
    }
}