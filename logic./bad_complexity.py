def bad_complexity(x):
    if x > 0:
        if x % 2 == 0:
            for i in range(x):
                if i % 3 == 0:
                    print(i)
