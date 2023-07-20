def Maximum_profit(arr):
    s = max(arr)
    j = min(arr)
    k = s-j
    return k
arr = list(map(int,input("Enter : ").split()))
print(Maximum_profit(arr))
