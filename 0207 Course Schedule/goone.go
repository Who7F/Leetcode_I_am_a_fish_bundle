func dfs(node int, states []int, graph map[int][]int) bool {
    if states[node] == 2 {
        return true
    }
    if states[node] == 1 {
        return false
    } 

    states[node] = 1
    
    for _, i := range graph[node]{
        if !dfs(i, states, graph) {
            return false
        }
    }
    

    states[node] = 2
    return true
}

func canFinish(numCourses int, prerequisites [][]int) bool {
    graph := make(map[int][]int)
    states := make([]int, numCourses)

    for _, pre := range prerequisites {
        graph[pre[0]] = append(graph[pre[0]], pre[1])
    }

    for i := 0; i< numCourses; i++{
        if !dfs(i, states, graph) {
            return false
        }
    }
    return true
}
