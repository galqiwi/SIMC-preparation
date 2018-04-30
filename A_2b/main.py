def dist(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

n = 3

res = []

for C in [(x, y) for x in range(0, n) for y in range(0, n)]:
	for D in [(x, y) for x in range(0, n) for y in range(0, n)]:
		for E in [(x, y) for x in range(0, n) for y in range(0, n)]:
			for F in [(x, y) for x in range(0, n) for y in range(0, n)]:
				maxd = 0
				for A in [(x, y) for x in range(0, n) for y in range(0, n)]:
					for B in [(x, y) for x in range(0, n) for y in range(0, n)]:
						lmin = dist(A, B)
						lmin = min(lmin, dist(A, C) + dist(D, B))
						lmin = min(lmin, dist(A, D) + dist(C, B))
						lmin = min(lmin, dist(A, E) + dist(F, B))
						lmin = min(lmin, dist(A, F) + dist(E, B))

						lmin = min(lmin, dist(A, C) + dist(D, E) + dist(F, B))
						lmin = min(lmin, dist(A, D) + dist(C, E) + dist(F, B))
						lmin = min(lmin, dist(A, C) + dist(D, F) + dist(E, B))
						lmin = min(lmin, dist(A, D) + dist(C, F) + dist(E, B))

						lmin = min(lmin, dist(A, E) + dist(F, C) + dist(D, B))
						lmin = min(lmin, dist(A, E) + dist(F, D) + dist(C, B))
						lmin = min(lmin, dist(A, F) + dist(E, C) + dist(D, B))
						lmin = min(lmin, dist(A, F) + dist(E, D) + dist(C, B))
						maxd = max(maxd, lmin)
				res = res + [(maxd, C, D, E, F)]
		print(C, D)

res = sorted(res)

out = open('out', 'w')

for i in res:
	print(i, file = out)

out.close()
