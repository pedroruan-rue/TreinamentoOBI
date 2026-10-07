simulations = int(input())

for i in range(simulations):
    number = int(input())
    meter = 0
    while True:
        if number%6 == 0:
            number = number/6
            meter += 1
        elif number == 1:
            break
        elif number%3 != 0: 
            meter = -1
            break
        else:
            number = number*2
            meter += 1
    print(meter)