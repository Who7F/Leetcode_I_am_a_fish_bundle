class MinStack {
private:
    using TempPair = pair<int, int>;
    stack<TempPair> stack;
public:
   
    void push(int val) {
        if (stack.empty()){
            stack.push(TempPair(val, val));
        }else{
            stack.push(TempPair(val, min(stack.top().second, val)));
        }
    }
    
    void pop() {
        stack.pop();
    }
    
    int top() {
        return stack.top().first;
    }
    
    int getMin() {
        return stack.top().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */