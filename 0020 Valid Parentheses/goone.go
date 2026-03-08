type Stack struct {
    arr []rune
}

func NewStack() *Stack {
    return &Stack {
        arr : []rune{},
    }
}

func (s *Stack) Push(value rune) {
    s.arr = append(s.arr, value)
}

func (s *Stack) Pop() (rune, bool) {
    if len(s.arr) == 0 {
        return 0, false
    }

    idx := len(s.arr) - 1
    value := s.arr[idx]
    s.arr[idx] = 0
    s.arr = s.arr[:idx]

    return value, true
}

func (s *Stack) Peek() (rune, bool) {
    if len(s.arr) == 0 {
        return 0, false
    }
    return s.arr[len(s.arr) - 1], true
}

func (s *Stack) Len() int {
    return len(s.arr) 
}

func isValid(s string) bool {
    stack := NewStack()
    pairs := map[rune]rune{'{':'}','[':']','(':')'}

    for _, c := range s {
        if val, ok := pairs[c]; ok {
            stack.Push(val)
        } else {
            v, ok := stack.Pop()
            if !ok || v != c {
                return false
            }
            
        }
    }

    return stack.Len() == 0
}