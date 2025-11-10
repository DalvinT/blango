# Burge's Solution – Boggle Solver using HashMap

import re


class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = set(word.upper() for word in dictionary)
        self.prefixes = self._build_prefixes(self.dictionary)
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.solutions = set()

    def _build_prefixes(self, words):
        prefixes = set()
        for word in words:
            for i in range(1, len(word)):
                prefixes.add(word[:i])
        return prefixes

    def get_solution(self):
        visited = [[False] * self.cols for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                self._dfs(r, c, self.grid[r][c].upper(), visited, [(r, c)])
        return sorted(self.solutions)

    def getSolution(self):  # For Codio test suite compatibility
        return self.get_solution()

    def _dfs(self, r, c, path, visited, positions):
        if len(path) >= 3 and path in self.dictionary:
            self.solutions.add(path)

        if path not in self.prefixes:
            return

        visited[r][c] = True

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < self.rows and
                    0 <= nc < self.cols and
                    not visited[nr][nc]
                ):
                    next_char = self.grid[nr][nc].upper()
                    self._dfs(nr, nc, path + next_char, visited, positions + [(nr, nc)])

        visited[r][c] = False
