def deep_decision(x):
    if x > 0:
        if x < 100:
            if x % 2 == 0:
                return "even"
            else:
                return "odd"
        else:
            return "large"
    else:
        return "negative"
