import sys
import time

# k, p, n = map(int, sys.stdin.readline().split(" "))
k = int(10e+8)
p = int(10e+6)
n = int(10e+5)

startTime = time.time()
print(int(k%1000000007 * pow(p, n, 1000000007))%1000000007)
print(int(k * pow(p, n))%1000000007)
endTime = time.time()
print("Execute time with pow:",(endTime-startTime)) # 0.00

startTime = time.time()
print(int((k*p**n)%1000000007))
endTime = time.time()
print("Execute time with **:",(endTime-startTime)) # 6.65