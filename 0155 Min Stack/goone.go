func min(x, y int) int {
    if x > y {
        return y
    }
    return x
}

type MinStack struct {
    stack []int
    minStack []int
}


func Constructor() MinStack {
    return MinStack{}    
}


func (this *MinStack) Push(val int)  {
    this.stack = append(this.stack, val)
    idx := len(this.minStack) - 1
    if idx >= 0 {
        val = min(val, this.minStack[idx])
    }
    this.minStack = append(this.minStack, val)
}


func (this *MinStack) Pop()  {
    idx := len(this.minStack) - 1
    this.stack = this.stack[:idx]
    this.minStack = this.minStack[:idx]
}


func (this *MinStack) Top() int {
    idx := len(this.minStack) - 1
    return this.stack[idx]
}


func (this *MinStack) GetMin() int {
    idx := len(this.minStack) - 1
    return this.minStack[idx]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */