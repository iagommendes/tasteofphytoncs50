def main():
    score1 = int(input("Score1: "))
    score2 = int(input("Score2: "))
    score3 = int(input("Score3: "))

    print_score(score1)
    print_score(score2)
    print_score(score3)

def print_score(n):
    for i in range(n):
        print("#", end="")
    print()
main()