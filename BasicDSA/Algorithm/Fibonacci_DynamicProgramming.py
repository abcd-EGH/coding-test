def fib_dp_mem(n):
    if n < 2:
        mem[n] = n
    else:
        mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)
    return mem[n]

def fin_dp_tab(n):
    f = [None] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i-1] + f[i-2]
    return f[:]

if __name__ == "__main__":
    target_value = 7
    mem = [None for _ in range(target_value + 1)]

    print("target value: ", target_value)
    print("fib. w/ memoization:", fib_dp_mem(target_value))
    print("fib. w/ tabulation:", fin_dp_tab(target_value))