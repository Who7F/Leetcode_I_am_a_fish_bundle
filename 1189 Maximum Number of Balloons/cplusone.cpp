class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> t;
        string s = "balloon";
        int n = 0;

        for (auto c : text) {
            t[c] ++;
        }

        for(;;) {
            for (auto b : string_view(s)){    
                if (--t[b] < 0) {
                    return n;
                } 
            }  
            n++;
        }

        return -1; //error
    }
};