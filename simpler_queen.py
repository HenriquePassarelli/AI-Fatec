
""" 
    ## requirements

    run - python3 simpler_queen.py

 """
def queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a


""" 8 queens were passed as arguments then returned the positions on each iteration"""
count = 0
for solution in queens(8, 0, [], [], []):
    count += 1
    print(solution)

print("\ndistinct solutions",count)