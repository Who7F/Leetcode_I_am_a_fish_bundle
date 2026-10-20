class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        n = len(words)
        hash_map = {}

        for ws in words:
            if len(ws) < k:
                continue

            p = ws[:k]
            hash_map[p] = hash_map.get(p, 0) + 1

        res = 0
        for h in hash_map.values():
            if h > 1:
                res += 1

        return resclass Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        n = len(words)
        hash_map = {}

        for ws in words:
            if len(ws) < k:
                continue

            p = ws[:k]
            hash_map[p] = hash_map.get(p, 0) + 1

        res = 0
        for h in hash_map.values():
            if h > 1:
                res += 1

        return res
