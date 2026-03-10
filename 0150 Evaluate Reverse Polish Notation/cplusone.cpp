class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> myStack;
        for(const auto& i : tokens){
            if (isdigit(i[0]) || (i[0] == '-' && i.size() > 1)){
                myStack.push(stoi(i));
            }
            else if(i == "+"){
                int top = myStack.top();
                myStack.pop();
                int bot = myStack.top();
                myStack.pop();
                myStack.push(bot + top);
            }
            else if(i == "-"){
                int top = myStack.top();
                myStack.pop();
                int bot = myStack.top();
                myStack.pop();
                myStack.push(bot - top);
            }
            else if(i == "*"){
                int top = myStack.top();
                myStack.pop();
                int bot = myStack.top();
                myStack.pop();
                myStack.push(bot * top);
            }
            else if(i == "/"){
                int top = myStack.top();
                myStack.pop();
                int bot = myStack.top();
                myStack.pop();
                myStack.push(bot / top);
            }
            else{
                return -1;
            }
        }
    return myStack.top();
    }
};