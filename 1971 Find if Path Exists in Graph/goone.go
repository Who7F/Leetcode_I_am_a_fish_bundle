func validPath(n int, edges [][]int, source int, destination int) bool {
    if source == destination {
            return true
        }
        gph := make(map[int][]int)
        for _, edge := range edges {
            gph[edge[0]] = append(gph[edge[0]], edge[1])
            gph[edge[1]] = append(gph[edge[1]], edge[0])
        }

        seen := make(map[int]bool)
        stack := []int{source}

        for len(stack) > 0 {
            node := stack[len(stack) - 1]
            stack = stack[:len(stack) - 1]

            if node == destination {
                return true
            }

            if seen[node] {
                continue
            } 
            seen[node] = true

            for _, n_node := range gph[node] {
                if !seen[n_node] {
                    stack = append(stack, n_node)
                }
            }
        }
        return false    
}

