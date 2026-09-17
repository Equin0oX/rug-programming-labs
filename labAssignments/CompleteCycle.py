def completeCycle(path):
    numbers = [int(number) for number in path.split(" ")]
    numbers_visited = []
    lastVisitedNumber = 0
    for i in range(len(numbers)):
        numbers_visited.append(numbers[i])
    if numbers_visited == numbers:
        return True
    return False

print(completeCycle(input()))