from random import randint

# Number of test cases
print('8')

# 2 Samples
# Expected output: 1 3
# Expected output: 2 4
print("""3 2 1 1
1 2
1 3
6 6 3 1
1 3
2 6
3 5
5 4
3 4
1 5""")

# Completely disconnected graph
# Expected output: 100000 1
print('100000 0 50 3')

# Completely connected graph
# Expected output: 1 500
print('500 124750 5 1')
for a in range(1, 501):
	for b in range(a + 1, 501):
		print(a, b)

# Linked list, starting at 1
# Expected output: 1 2
ll_size = 1000
print(ll_size, ll_size - 1, 1, 1)
for i in range(2, ll_size + 1):
    print(i - 1, i)

# Linked list, starting at 2
# Expected output: 1 3
ll_size = 1000
print(ll_size, ll_size - 1, 2, 1)
for i in range(2, ll_size + 1):
    print(i - 1, i)


# 4 different connected (non-singular) components 
# Expected output: 64 3
print(200, 19 + 29 + 1225 + 780, 15, 1)
# 0 through 19 connected in linked list style
for a in range(1, 20):
	print(a, a + 1)
# 20 through 49 connected in linked list style
for a in range(21, 50):
	print(a, a + 1)
# 50 through 99 completely connected
for a in range(51, 101):
	for b in range(a + 1, 101):
		print(a, b)
# 100 through 139 completely connected 
for a in range(101, 141):
	for b in range(a + 1, 141):
		print(a, b);

# Sets of 5
# Expected Output: 40 5
print('200 160 1 5')
for a in range(1, 201, 5):
	for b in range(a, a + 4):
		print(b, b + 1)

"""
# Random big graph
n = 100000
m = 200000
start = 3
dist = 50
print(n, m, start, dist)
edges = set()
for _ in range(m):
    x = randint(1, n - 1)
    y = randint(x + 1, n)
    while (x, y) in edges:
        x = randint(1, n - 1)
        y = randint(x + 1, n)

    edges.add((x, y))
    if randint(1, 2) == 1:
        print(x, y)
    else:
        print(y, x)
"""
