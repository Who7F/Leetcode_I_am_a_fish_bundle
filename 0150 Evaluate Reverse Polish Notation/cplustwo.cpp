class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for(const auto& t : tokens){
            if (isdigit(t[0]) || (t[0] == '-' && t.size() > 1)){
                s.push(stoi(t));
            }
            else {
                int y = s.top(); s.pop();
                int x = s.top(); s.pop();
                switch (t[0]) {
                    case '+': s.push(x + y); break;
                    case '-': s.push(x - y); break;
                    case '*': s.push(x * y); break;
                    case '/': s.push(x / y); break;
                }
            }            
        }
    return s.top();
    }
};