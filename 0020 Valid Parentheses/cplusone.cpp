class Solution {
public:
    bool isValid(string s) {
        map<char, char> myMap;
        stack<char> myStack;
        myMap['{'] = '}';
        myMap['['] = ']';
        myMap['('] = ')';
        for(const auto& i : s){
            if(myMap.contains(i)) myStack.push(myMap[i]);
            else if(myStack.empty() || myStack.top() != i) return false;
            else myStack.pop();    
        }
        return myStack.empty();
    }
};