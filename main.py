COUNTER_COMPARES = 0
COUNTER_SWITCHES = 0


def insertionSort(numbers):

    for i in range(1, len(numbers)):
        tmp = numbers.pop(i)

        for j in range(i, 0, -1):
            if tmp > numbers[j-1]:
                numbers.insert(j, tmp)
                break
            if j == 1:
                numbers.insert(j-1, tmp)

    return numbers
