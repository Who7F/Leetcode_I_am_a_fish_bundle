class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        using TempPairMagic = pair<int, int>;
        vector<int> anc(temperatures.size());
        stack<TempPairMagic> stack;
        for(int i = 0; i < temperatures.size(); i++){
            while(!stack.empty() && temperatures[i] > stack.top().second){  
                anc[stack.top().first] = i - stack.top().first;
                stack.pop();
            }
            stack.push(TempPairMagic(i, temperatures[i]));
        }
        return anc;
    }
};