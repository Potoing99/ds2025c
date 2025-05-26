from collections import deque   # bfs (append, popleft)

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def dfs(g, i, visited):#깊이 우선 탐색 ==> stack or 재귀함수
    visited[i] = 1
    print(chr(ord('A') + i), end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)#



def bfs(g, i, visited):#너비 우선 탐색 ==> 반복문 or queue
   q = deque([i])
   visited[i] = 1
   while q:
       i = q.popleft()
       print(chr(ord('A') + i), end = ' ')
       for j in range(len(graph)):
           if g[i][j] == 1 and not visited[j]:
               q.append(j)
               visited[j] = 1


#그래프 그림 그려보면 이해가 빠름 그려보기
visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]
dfs(graph, 4, visited_dfs)
print()
bfs(graph, 4, visited_bfs)  #i = 시작 인덱스 번호