class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> stack;
        for(const auto& i : operations){
            if(i == "+")
                stack.push_back(stack.back() + stack[stack.size() - 2]);
            else if(i == "D")
                stack.push_back(2 * stack.back());
            else if(i == "C")
                stack.pop_back();
            else
                stack.push_back(stoi(i)); 
        }
        int sum = 0;
        for (int i : stack){
            sum += i;
        }
        return sum;
    }
};