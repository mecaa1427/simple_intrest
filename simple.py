def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


if __name__ == "__main__":
    p = int(input("enter value of p:"))
    i = int(input("enter value of i"))
    t =int(input("enter time"))
    print("Simple Interest:", simple_interest(p, i, t))