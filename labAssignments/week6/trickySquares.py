def count_tricky_squares(lower, upper):
    start = int(lower ** 0.5)
    end = int(upper ** 0.5) + 1

    count = 0
    for root in range(start, end + 1):
        square = root * root
        if square < lower or square > upper:
            continue

        text = str(square)
        repeated_digits = 0
        for digit in "0123456789":
            if text.count(digit) > 1:
                repeated_digits += 1

        if repeated_digits == 1:
            count += 1

    return count


lower, upper = map(int, input().split())
print(count_tricky_squares(lower, upper))
