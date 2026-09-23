import random
import time
import sys
sys.setrecursionlimit(20000)
comparisons = 0
def partition(arr, low, high):
global comparisons
pivot = arr[high]
i = low - 1
for j in range(low, high):
comparisons += 1
if arr[j] &lt;= pivot:
i += 1
arr[i], arr[j] = arr[j], arr[i]
arr[i + 1], arr[high] = arr[high], arr[i + 1]
return i + 1
def deterministic_quicksort(arr, low, high):
if low &lt; high:
pi = partition(arr, low, high)
deterministic_quicksort(arr, low, pi - 1)
deterministic_quicksort(arr, pi + 1, high)
def randomized_quicksort(arr, low, high):
if low &lt; high:
# Randomize pivot
rand_idx = random.randint(low, high)
arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
pi = partition(arr, low, high)
randomized_quicksort(arr, low, pi - 1)
randomized_quicksort(arr, pi + 1, high)
def run_test(name, sort_fn, arr):
global comparisons
a = arr[:]
comparisons = 0
start = time.perf_counter()
sort_fn(a, 0, len(a) - 1)
elapsed = (time.perf_counter() - start) * 1000
return comparisons, elapsed
N = 5000
test_cases = {
&#39;Random&#39; : [random.randint(1, 100000) for _ in range(N)],
&#39;Sorted&#39; : list(range(N)),
&#39;Reverse&#39; : list(range(N, 0, -1)),
&#39;Nearly Sorted&#39;: list(range(N))
}
# Make Nearly Sorted slightly shuffled
ns = test_cases[&#39;Nearly Sorted&#39;]
for _ in range(N // 20):
i, j = random.randint(0, N-1), random.randint(0, N-1)
ns[i], ns[j] = ns[j], ns[i]
print(f&#39;{&#39;Input Type&#39;:&lt;16} {&#39;DQS Comps&#39;:&gt;12} {&#39;DQS Time(ms)&#39;:&gt;14} &#39;&quot;,&quot;
f&#39;{&#39;RQS Comps&#39;:&gt;12} {&#39;RQS Time(ms)&#39;:&gt;14}&#39;)
print(&#39;-&#39; * 72)
for case, arr in test_cases.items():
      d_comps, d_time = run_test(&#39;DQS&#39;, deterministic_quicksort, arr)
r_comps, r_time = run_test(&#39;RQS&#39;, randomized_quicksort, arr)
print(f&#39;{case:&lt;16} {d_comps:&gt;12} {d_time:&gt;14.2f} {r_comps:&gt;12} {r_time:&gt;14.2f}&#39;)
