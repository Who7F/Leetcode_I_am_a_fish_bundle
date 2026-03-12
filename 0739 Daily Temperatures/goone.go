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
    res := s.arr[idx]
    s.arr = s.arr[:idx]

    return res, true
}

func (s *Stack) Empty() bool {
    if len(s.arr) == 0 {
        return true
    }
    return false
}

func (s *Stack) Peek() (int, bool) {
    if len(s.arr) == 0 {
        return 0, false
    }
    idx := len(s.arr) - 1
    res := s.arr[idx]

    return res, true
}


func dailyTemperatures(temperatures []int) []int {
    stack := NewStack()
    res := make([]int, len(temperatures))

    for idx, tmp := range temperatures {
        for !stack.Empty(){
            top, _ := stack.Peek()

			if temperatures[top] >= tmp {
				break
			}

            tmp, _ := stack.Pop()
            res[tmp] = idx - tmp
        }
        stack.Push(idx)
    }
    return res
}