/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
    if node == nil {
        return nil
    }
    seen := make(map[*Node]*Node)
    que := []*Node{node}

    seen[node] = &Node{Val: node.Val}

    for len(que) > 0 {
        curr := que[0]
        que = que[1:]
        for _, n := range curr.Neighbors {
            if _, poo := seen[n]; !poo {
                seen[n] = &Node{Val: n.Val}
                que = append(que, n)
            }
            seen[curr].Neighbors = append(seen[curr].Neighbors, seen[n]) 
        }
    }

    return seen[node]
}