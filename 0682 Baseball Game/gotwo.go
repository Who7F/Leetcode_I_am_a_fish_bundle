type Stack struct {
    arr []int
}

func NewStack() *Stack {
    return &Stack{
        arr: []int{},
    }
}

func (s *Stack) Push(value int) {
    s.arr = append(s.arr, value)
}

func (s *Stack) Pop() (int, bool) {
    if len(s.arr) == 0 {
        return 0, false
    }

    // idx := len(s.arr)-1. But simple code so I am going to be laze
    val := s.arr[len(s.arr)-1]
    s.arr[len(s.arr)-1] = 0 // clear element (important if slice stores pointers)
    s.arr = s.arr[:len(s.arr)-1]

    return val, true
}

func (s *Stack) Peek() (int, bool) {
    if len(s.arr) == 0 {
        return 0, false
    }
    return s.arr[len(s.arr)-1], true
}

func (s *Stack) Len() int {
    return len(s.arr)
}

func sum(values []int) int {
    res := 0
    for _, v := range values {
        res += v
    }
    return res
}


func calPoints(operations []string) int {
    stack := NewStack()

    for _, op := range operations {
        switch op {

        case "C":
            stack.Pop()

        case "D":
            v, _ := stack.Peek()
            stack.Push(v * 2)

        case "+":
            last := stack.arr[len(stack.arr)-1]
            prev := stack.arr[len(stack.arr)-2]
            stack.Push(last + prev)

        default:
            n, _ := strconv.Atoi(op)
            stack.Push(n)
        }
    }

    return sum(stack.arr)
}