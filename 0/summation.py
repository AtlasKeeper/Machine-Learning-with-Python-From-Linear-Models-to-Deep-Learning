def compute(N):
    return sum(1 for i in range(N + 1))

N = 5
result = compute(N)

print(f"The answer is: {result}")