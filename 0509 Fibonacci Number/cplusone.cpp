class Solution {
public:
    int fib(int n) {
        if(n < 2) return n;

        int a = 0;
        int b = 1;

        for (int i = 1; i < n; i++) {
            int temp = b;
            b = a + b;
            a = temp;
        }

        return b;      
    }
};