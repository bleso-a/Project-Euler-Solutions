#Write a function that computes the sum of multiple of 3 and 5, range of 1000
def compute():
    mul = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return str(mul)


if __name__ == "__main__":
    print(compute())
