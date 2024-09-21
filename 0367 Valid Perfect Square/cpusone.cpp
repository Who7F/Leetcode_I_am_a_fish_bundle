class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num == true) return true;
        int64_t n = num;
        int64_t lit = 0;
        while(lit < n){
            int64_t cnt = lit + (n - lit)/2;
            if(cnt*cnt == num)
                return true;
            else if(cnt*cnt > num)
                n = cnt;
            else
                lit = cnt + 1;
        }
        return false;    
    }
};