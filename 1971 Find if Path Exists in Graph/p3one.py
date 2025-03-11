class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        gph = defaultdict(list)
        for u, v in edges:
            gph[u].append(v)
            gph[v].append(u)

        seen = set()
        seen.add(source)
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for n_node in gph[node]:
                if n_node not in seen:
                    seen.add(n_node)
                    stack.append(n_node)

        return False
