def first_fit(items, capacity=1.0):
bins = [] # Each bin stores remaining space
bin_contents = []
for item in items:
placed = False
for i, space in enumerate(bins):
if space &gt;= item:
bins[i] -= item
bin_contents[i].append(item)
placed = True
break
if not placed:
bins.append(capacity - item)
bin_contents.append([item])
return bin_contents
def first_fit_decreasing(items, capacity=1.0):
return first_fit(sorted(items, reverse=True), capacity)
def best_fit_decreasing(items, capacity=1.0):
sorted_items = sorted(items, reverse=True)
bins = []
bin_contents = []
for item in sorted_items:
best_idx = -1
best_space = float(&#39;inf&#39;)
for i, space in enumerate(bins):
if space &gt;= item and space - item &lt; best_space:
best_space = space - item
best_idx = i
if best_idx &gt;= 0:
bins[best_idx] -= item
bin_contents[best_idx].append(item)
else:
bins.append(capacity - item)
bin_contents.append([item])
return bin_contents
def display_bins(label, bins):
print(f&#39;\n{label}: {len(bins)} bins&#39;)
for i, b in enumerate(bins, 1):
used = sum(b)
bar = &#39;#&#39; * int(used * 20)
print(f&#39; Bin {i}: {[round(x,1) for x in b]} | Used: {used:.1f} &#39;&quot;,&quot;
f&#39;[{bar:&lt;20}]&#39;)
items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
capacity = 1.0
lower_bound = -(-sum(items) // capacity) # Ceiling division
print(f&#39;Items: {items}&#39;)
print(f&#39;Capacity: {capacity}&#39;)
print(f&#39;Sum of items: {sum(items)}&#39;)
print(f&#39;Lower bound on bins: {int(lower_bound)}&#39;)
ff_bins = first_fit(items)
ffd_bins = first_fit_decreasing(items)
bfd_bins = best_fit_decreasing(items)
display_bins(&#39;First Fit (FF)&#39;, ff_bins)
display_bins(&#39;First Fit Decreasing (FFD)&#39;, ffd_bins)
display_bins(&#39;Best Fit Decreasing (BFD)&#39;, bfd_bins)
print(f&#39;\nSummary: Lower Bound={int(lower_bound)}, FF={len(ff_bins)},
FFD={len(ffd_bins)}, BFD={len(bfd_bins)}&#39;)
