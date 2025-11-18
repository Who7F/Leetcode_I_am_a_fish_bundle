class Solution:
    def getFib(self, magic_fib, i, n):

        if i == n: return
        magic_fib.append(magic_fib[i] + magic_fib[i-1])

        self.getFib(magic_fib,  i+1 ,n)

    def fib(self, n: int) -> int:
        if n < 2:
            return n

        magic_fib = [0, 1]
        self.getFib(magic_fib,  1 ,n)
        return magic_fib[n]