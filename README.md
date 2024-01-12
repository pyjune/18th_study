# 18th_study

### 18주차 알고리즘스터디

# 지난주 문제

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [문자의 빈도](https://www.codetree.ai/problems/frequency-of-characters/description)

### [민웅](<./문자의 빈도/민웅.py>)

```py


```

### [상미](<./문자의 빈도/상미.py>)

```py

```

### [병국](<./문자의 빈도/병국.py>)

```py

```

### [성구](./문자의%빈도/성구.py)

```py

```

<br/><br/>

## [코드트리 마트](https://www.codetree.ai/problems/codetree-market/description)

### [민웅](./코드트리%마트/민웅.py)

```py

```

### [상미](./코드트리%마트/상미.py)

```py


```

### [병국](./코드트리%마트/병국.py)

```py

```

### [성구](./코드트리%마트/성구.py)

```py

```

<br>

## [기차 놀이](https://www.codetree.ai/problems/train-game/description)

### [민웅](<./기차 놀이/민웅.py>)

```py


```

### [상미](<./기차 놀이/상미.py>)

```py

```

### [병국](<./기차 놀이/병국.py>)

```py

```

### [성구](./기차%놀이/성구.py)

```py

```

<br/><br/>

</div>




</details>

</br></br></br>

# 이번주 문제

<details open>
<summary>접기/펼치기</summary>
<div markdown="1">

## [사다리 조작](https://www.acmicpc.net/problem/15684)

### [민웅](<./사다리 조작/민웅.py>)

```py
```

### [상미](<./사다리 조작/상미.py>)

```py

```

### [병국](<./사다리 조작/병국.py>)

```py

```

### [성구](<./사다리 조작/성구.py>)

```py
# 15684 사다리 조작
import sys
input = sys.stdin.readline


def check_ladder() -> bool:
    for i in range(N):
        y, x = 0, i
        while y < H:
            if ladders[y][x] == 1:      # 1이면 왼쪽으로 이동
                x -= 1
            elif ladders[y][x] == 2:    # 2면 오른쪽으로 이동
                x += 1
            y += 1
        if x != i:      # i -> i 가 아닐경우 False
            return 0       
    return 1        # 모두 i -> i 되면 True

# 백트래킹
def bt(cnt:int, start_i:int) -> None:
    global ans
    
    if check_ladder():  # i-> i 체크
        # 된다면 cnt 저장
        ans = min(cnt, ans)
        return
    if cnt == 3:        # 3 이하일 때만 허용
        return 
    if cnt >= ans:
        return
    # i -> i가 안 될 경우, 탐색 중이었던 높이부터 체크하면 됨
    for i in range(start_i, H):
        for j in range(N-1):
            if not ladders[i][j] and not ladders[i][j+1]:
                ladders[i][j] = 2
                ladders[i][j+1] = 1
                bt(cnt+1, i)
                ladders[i][j] = 0
                ladders[i][j+1] = 0
    return


if __name__ == "__main__":
    N, M, H = map(int, input().split())
    ladders = [[0] * N for _ in range(H)]
    visited = [[0] * N for _ in range(H)]
    for _ in range(M):
        # 1 -> 왼쪽, 2 -> 오른쪽
        a, b = map(int, input().split())
        ladders[a-1][b-1] = 2
        ladders[a-1][b] = 1
    ans = 5
    bt(0,0)
    print(-1 if ans > 3 else ans)
        
```

</div>
</details>
<br><br>

# 알고리즘 설명

<details>
<summary>접기/펼치기</summary>

## 용어 정리

### Spanning Tree (신장 트리)

- **정의**: 주어진 그래프의 모든 정점을 포함하면서 사이클이 없는 부분 그래프.
- **중요성**: 신장 트리를 통해 그래프의 구조를 단순화시키고, 필요한 정보만을 추출하기 위함
- **속성**:
  - 원래 그래프의 모든 정점을 포함해야한다.
  - 정확히 (정점 수 - 1)개의 간선을 가져야한다.
  - 사이클을 형성하지 않는다.

### Minimum Spanning Tree (최소 신장 트리)

![MST](./images/mst.png)

- **정의**: 가능한 신장 트리(Spanning Tree) 중에서 간선의 가중치 합이 최소인 신장 트리.
- **중요성**: 최소 비용 문제를 해결하는 데 사용되며 주로 **네트워크 설계**, **도로 건설**, **전력망 구축** 등 다양한 분야에서 응용가능
- **대표알고리즘 예**: [Kruskal 알고리즘](#Kruskal-알고리즘), [Prim 알고리즘](#prim-알고리즘).
- **속성**:
  - 모든 정점을 포함하면서 최소한의 비용으로 연결합니다.
  - 가중치가 가장 낮은 간선부터 선택하여 구성한다.(그리디 방법).

## 대표 알고리즘

### Kruskal 알고리즘

- **탐색 방법**: 가장 가벼운 가중치의 간선부터 선택하여 MST를 찾는 알고리즘.
- **구현 방법**
  1. 간선 정렬 및 정점 초기화
  2. 간선 선택 후 정점 병합
  3. n-1개의 간선이 선택될 때까지(모든 정점이 선택될 때까지) 2번단계 반복

```py
# 구현

# 주어진 노드의 루트노드 반환
# 부모노드를 찾아가며, 루트노드(자기 자신을 가리키고있는 노드)를 찾음
def findset(node):
    while parent[node] != node:
        node = parent[node]
    return node

# x, y 노드를 같은 그룹으로 병합
def union(x, y):
    parent[findset(y)] = findset(x)

def kruskal(graph, V):
    # 그래프의 간선을 가중치에 따라 오름차순으로 정렬
    graph.sort(key=lambda x: x[2])

    # 각 정점에 대한 부모 초기화
    parent = [i for i in range(V+1)]

    mst = []
    total_cost = 0

    for edge in graph:
        u, v, weight = edge
        # 사이클이 형성되지 않는 경우에만 간선 선택
        if findset(u) != findset(v):
            union(u, v)
            mst.append(edge)
            total_cost += weight

    return mst, total_cost

graph = []
for _ in range(M):
    s, g, w = map(int, input().split())
    graph.append([s, g, w])

kruskal(graph, V)

```

### Prim 알고리즘

- **탐색 방법**: 시작 정점에서부터 점차 그래프를 확장해 나가며 MST를 찾는 알고리즘.
- **구현 방법**
  1. 임의의 시작정점 선택 후 간선그룹 생성(heapq)
  2. 간선 선택 - MST 집합에 속한 정점과 속하지 않은 정점을 연결하는 간선 중 최소가중치 간선을 선택함.
  3. 추가된 정점에 연결된 새로운 간선 추가 및 2번 과정 반복
  4. 큐가 비거나 모든정점이 MST에 포함되면 종료

```py
# 구현
import heapq

def prim(graph, start, V):
    visited = [0] * (V+1)
    min_heap = [(0, start)]  # (가중치, 정점)
    total_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if not visited[u]:
            visited[u] = 1
            total_cost += weight
            for v, w in graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))

    return total_cost

graph = [[] for _ in range(V+1)]
# 그래프에 정점 별 간선정보 (u, v, w) 추가
cost = prim(graph, 1, V)

```

## Kruskal vs Prim (https://8iggy.tistory.com/160)

- 희소 그래프: 정점들 사이에 간선이 상대적으로 적게 존재하는 그래프. 예를 들어, 정점의 수에 비해 간선의 수가 훨씬 적은 경우.

- 밀집 그래프: 정점들 사이에 많은 수의 간선이 존재하는 그래프. 거의 모든 정점 쌍 사이에 간선이 존재하는 경우.

### Kruskal

-> 간선의 수가 적은 희소 그래프에 적합. 연결 요소 파악에 유용.

장점:

- 구현이 간단하고 메모리 사용이 효율적.
- 간선의 수가 적을수록 더 효과적.

단점:

- 간선의 수가 많은 밀집 그래프에서는 비효율적.
- 모든 간선을 정렬해야 하므로 초기에 시간이 소요됨.

### Prim

-> 간선의 수가 많은 밀집 그래프에 적합. 작은 그래프에서 빠른 성능.

장점:

- 밀집 그래프에서 효율적.
- 최소 힙을 사용하여 동적으로 간선 선택 가능.

단점:

- 메모리 사용량이 더 많음.
- 정점의 수가 많을수록 성능 저하 가능성 있음.

</details>
