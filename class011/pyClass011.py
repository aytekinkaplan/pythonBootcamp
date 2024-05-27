def greeting(*name):
    for n in name:
        print(f"Hello {n}!")
    for n in name:
        print(f"Good Morning {n}!")


greeting("James", "Michael", "Henry", "Thomas")


def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3, 4, 5))
