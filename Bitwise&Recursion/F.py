def play(n, orig, aux, dest):
    if n == 1:
        print(f"{orig} {dest}")
        return
    play(n-1, orig, dest, aux)

    print(f"{orig} {dest}")

    play(n-1, aux, orig, dest)


n = int(input())
moves = 2**n - 1

print(moves)
play(n, 1, 2, 3)