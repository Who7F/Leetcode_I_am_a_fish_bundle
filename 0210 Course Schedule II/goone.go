func dfs(node int, state []int, graph map[int][]int, my_list *[]int) bool {
    if state[node] == 2 {
        return true
    }
    if state[node] == 1 {
        return false
    }
    state[node] = 1

    for _, i := range graph[node] {
        if !dfs(i, state, graph, my_list) {
            return false
        }
    }

    state[node] = 2
    *my_list = append(*my_list, node)
    return true 
}

func findOrder(numCourses int, prerequisites [][]int) []int {
    graph := make(map[int][]int)
    state := make([]int, numCourses)
    my_list := []int{}

    for _, p := range prerequisites{
        graph[p[0]] = append(graph[p[0]], p[1])
    }

    for i := 0; i < numCourses; i++{
        if !dfs(i, state, graph, &my_list){
            return []int{}
        }
    }
    return my_list
}