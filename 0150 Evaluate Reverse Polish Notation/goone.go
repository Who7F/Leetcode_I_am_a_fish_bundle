type Stack struct {
    arr []int
}

func NewStack() *Stack {
    return &Stack{
        arr: []int{},
    }
}

func (s *Stack) Push(val int) {
    s.arr = append(s.arr, val)
}

func (s *Stack) Pop() (int, bool) {
    if len(s.arr) == 0 {
        return 0, false
    }  
    idx := len(s.arr) - 1
    val := s.arr[idx]
    s.arr = s.arr[:idx]

    return val, true
}

func (s *Stack) Peek() (int, bool) {
    if len(s.arr) == 0 {
        return 0, false
    }
    idx := len(s.arr) - 1
    return s.arr[idx], true
}

func evalRPN(tokens []string) int {
    stack := NewStack()
    
    for _, t := range tokens {

        switch t {
            case "+":
                y, _ := stack.Pop()
                x, _ := stack.Pop()
                stack.Push(x + y)
            case "-":
                y, _ := stack.Pop()
                x, _ := stack.Pop()
                stack.Push(x - y)
            case "*":
                y, _ := stack.Pop()
                x, _ := stack.Pop()        
                stack.Push(x * y)
            
            case "/":
                y, _ := stack.Pop()
                x, _ := stack.Pop()
                stack.Push(x / y)
            default:
                n, _ := strconv.Atoi(t)
                stack.Push(n)
        }
    }
    res, _ := stack.Peek()
    return res
}