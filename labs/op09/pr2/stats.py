def statistics(numbers):
    total = 0
    biggest = numbers[0]
    for x in numbers:
        total = total + x
        if x > biggest:
            biggest = x
    average = total / len(numbers)
    return biggest, average


print(statistics([4, 9, 2, 7]))
