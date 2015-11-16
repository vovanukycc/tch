

def is_prime(x):
    if x > 2:
        for i in range(2, x):
            print(i)
            if x % i == 0:
                return False
        return True
    elif x == 2:
        return True
    else:
        return False


print(is_prime(13))