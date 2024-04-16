import random


def main():
    input_level = get_level()
    print("Score:",calculate(input_level))



def get_level():
    # Continue to prompt the user for level until a positve number is given
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                break
        except ValueError:
            continue
    return level


def generate_integer(level):
    # Generate random numbers from different ranges based on the level inputed
    range = level -1
    start = [0, 10, 100]
    end = [9, 99, 999]
    return random.randint(start[range], end[range])



def calculate(level):
    # The user starts off with 10 points and gets 3 attepts per problem.
    score = int(10)
    for i in range(10):
        x = int(generate_integer(level))
        y = int(generate_integer(level))
        tries = int(3)
        while tries != 0:
            try:
                answer = int(input("{} + {} = ".format(x, y)))
                if answer != (x+y):
                    print("Incorrect")
                    tries -= 1
                else:
                    break
            except ValueError:
                continue
        if tries == 0:
            print("{} + {} = {}".format(x, y, (x+y)))
            score -= 1
    return score



if __name__ == "__main__":
    main()