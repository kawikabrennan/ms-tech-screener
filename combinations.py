from itertools import combinations


def print_sum_combinations(numbers: list, specified_sum: int):
    results = []

    if specified_sum != 0:
        for number in range(len(numbers)):
            for combination in combinations(enumerate(numbers), number):
                sum_of_values = 0
                for _, value in combination:
                    sum_of_values += value
                if sum_of_values == specified_sum:
                    result = " ".join([str(index[0]) for index in combination])
                    results.append(result)
                    print(result)

    return results
