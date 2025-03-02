def bfs(si, sj, ei, ej):
    queue = []
    queue.append((si, sj))
    visited[si][sj] = 1

    while queue:
        r, c = queue.pop(0)
        if r == ei and c == ej:
            return visited[r][c]

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            di = r + dr
            dj = c + dc
            if 0 <= di < N and 0 <= dj < M and visited[di][dj] == 0 and maze[di][dj] == 1:
                queue.append((di, dj))
                visited[di][dj] = visited[r][c] + 1

N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

answer = bfs(0, 0, N-1, M-1)

print(answer)