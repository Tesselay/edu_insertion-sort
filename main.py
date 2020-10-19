COUNTER_COMPARES = 0
COUNTER_SWITCHES = 0


def insertionSort(numbers):
    global COUNTER_COMPARES
    global COUNTER_SWITCHES

    for i in range(1, len(numbers)):
        tmp = numbers.pop(i)

        for j in range(i, 0, -1):
            COUNTER_COMPARES += 1
            if tmp > numbers[j-1]:
                numbers.insert(j, tmp)
                COUNTER_SWITCHES += 1
                break
            if j == 1:
                numbers.insert(j-1, tmp)
                COUNTER_SWITCHES += 1
            # The counter only goes up, if the break in the first conditional doesn't fire
            COUNTER_COMPARES += 1

    print("Compares: {}".format(COUNTER_COMPARES))
    print("Switches: {}".format(COUNTER_SWITCHES))

    COUNTER_COMPARES = 0
    COUNTER_SWITCHES = 0

    return numbers
