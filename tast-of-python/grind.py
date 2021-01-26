def main():
    number = int(input("type a number of blocks: "))

    printscore(number)


def printscore(n):
    for i in range(n):
        for j in range (n):
            print("#", end="")
        print()

main()