def algoritmo(n):
    if n == 1:
        return str(n)
    elif n & 1:
        return str(n) + " " + algoritmo(n*3+1)
    else:
        return str(n) + " " + algoritmo(n>>1)

n = int(input())
print(algoritmo(n))