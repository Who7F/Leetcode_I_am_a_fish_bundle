class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> max_heap;

        for (int i : stones)
            max_heap.push(i);

        while (max_heap.size() > 1 && !max_heap.empty()) {
            int x = max_heap.top();
            max_heap.pop();
            int y = max_heap.top();
            max_heap.pop();
            //std::cout << x << ' ' << y << "\n";
            if (x != y) {
                max_heap.push(x - y);
            }
        }
        if (max_heap.size() == 1) {
            return max_heap.top();
        }
        return 0;
    }
};