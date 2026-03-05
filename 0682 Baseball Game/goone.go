func calPoints(operations []string) int {
    stack := []int{}

    for _, op := range operations {
        if op == "C" {
            stack = stack[:len(stack) - 1]
        } else if op == "D" {
            stack = append(stack, 2 * stack[len(stack) - 1])
        } else if op == "+" {
            stack = append(stack, stack[len(stack) - 1] + stack[len(stack) - 2])
        } else {
            num, _ := strconv.Atoi(op)
            stack = append(stack, num)
        }
    }

    res := 0
    for _, s := range stack {
        res += s
    }

    return res
}