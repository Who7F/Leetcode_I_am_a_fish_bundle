type Stack[T any] struct {
	arr []T
}

func NewStack[T any]() *Stack[T] {
	return &Stack[T]{
		arr: []T{},
	}
}

func (s *Stack[T]) Push(value T) {
	s.arr = append(s.arr, value)
}

func (s *Stack[T]) Pop() (T, bool) {
	var zero T

	if len(s.arr) == 0 {
		return zero, false
	}

	idx := len(s.arr) - 1
	value := s.arr[idx]
	s.arr = s.arr[:idx]

	return value, true
}