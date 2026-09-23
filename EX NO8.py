import heapq
from itertools import permutations
INF = float(&#39;inf&#39;)
def reduce_matrix(mat):
&quot;&quot;&quot;Reduce matrix and return reduction cost&quot;&quot;&quot;
import copy
m = [row[:] for row in mat]
n = len(m)
cost = 0
# Row reduction
for i in range(n):
row_min = min(m[i])
if row_min and row_min != INF:
cost += row_min
m[i] = [x - row_min if x != INF else INF for x in m[i]]
# Column reduction
for j in range(n):
col_min = min(m[i][j] for i in range(n))
if col_min and col_min != INF:
cost += col_min
for i in range(n):
if m[i][j] != INF:
m[i][j] -= col_min
return m, cost
def tsp_brute_force(cost, n):
&quot;&quot;&quot;Brute force for verification&quot;&quot;&quot;
cities = list(range(1, n))
best_cost = INF
best_path = None
for perm in permutations(cities):
path = [0] + list(perm) + [0]
c = sum(cost[path[i]][path[i+1]] for i in range(n))
if c &lt; best_cost:
best_cost = c
best_path = path
return best_path, best_cost
# --- 5-city cost matrix ---
cost = [
[INF, 10, 8, 9, 7],
[ 10, INF, 10, 5, 6],
[ 8, 10, INF, 8, 9],
[ 9, 5, 8, INF, 6],
[ 7, 6, 9, 6, INF]
]
n = 5
cities = [&#39;A&#39;, &#39;B&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;]
best_path, best_cost = tsp_brute_force(cost, n)
print(&#39;5-City TSP - Cost Matrix:&#39;)
print(f&#39;{&quot;&quot;:&gt;4}&#39;, &#39; &#39;.join(f&#39;{c:&gt;5}&#39; for c in cities))
for i, row in enumerate(cost):
r = [&#39;INF&#39; if x == INF else str(x) for x in row]
print(f&#39;{cities[i]:&gt;4}&#39;, &#39; &#39;.join(f&#39;{v:&gt;5}&#39; for v in r))
print(f&#39;\nOptimal Tour: {&quot; -&gt; &quot;.join(cities[i] for i in best_path)}&#39;)
print(f&#39;Minimum Cost: {best_cost}&#39;)
print(f&#39;\nPath verification:&#39;)
for i in range(n):
      u, v = best_path[i], best_path[i+1]
print(f&#39; {cities[u]} -&gt; {cities[v]}: cost = {cost[u][v]}&#39;)
