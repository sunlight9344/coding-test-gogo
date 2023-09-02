N,K = map(int,input().split())
array = list(map(int,input()))

stack_len = N-K

stack = []

for k in array:

    while stack:
        if stack[-1] >= k or not K:
            break
        stack.pop()
        K -= 1
    if len(stack) < stack_len:
        stack.append(k)

for a in stack:
    print(a,end='')