import sys

def is_happy(val):
    """Check whether a number is a happy number."""
    seen = set()
    while val != 1 and val not in seen:
        seen.add(val)
        val = sum([int(x) ** 2 for x in str(val)])

    return val == 1

def find_happy(N):
    """Return the first N happy numbers."""
    return [i for i in range(N) if is_happy(i)]

if __name__=="__main__":
    print(find_happy(int(sys.argv[1]) + 1))
