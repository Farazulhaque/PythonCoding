num_siblings = (
    1, 1, 2, 6, 2, 1, 1, 1, 2, 1, 3, 7, 8, 1, 2, 4, 2, 1, 4, 2, 2, 3, 2, 2, 2, 1,
    0, 2, 3, 1, 1, 1, 1, 1, 2, 2, 2, 1,
    3, 1, 2, 0, 2, 1, 1, 1, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 4, 0, 1, 3, 3, 4,
    1, 1, 1, 2, 1, 0, 1, 6, 1, 2
)
num_credits = (
    10, 16, 13, 13, 16, 16, 12, 12, 13, 18, 15, 14, 16, 16, 12, 12, 16, 16, 12, 12,
    16, 8, 12, 16, 16, 12, 16, 16, 16,
    16, 12, 14, 17, 17, 12, 17, 12, 16, 12, 12, 16, 18, 12, 16, 16, 16, 16, 16, 12,
    16, 13, 16, 15, 12, 12, 17, 17, 16,
    12, 16, 16, 16, 16, 12, 16, 17, 16, 16, 21, 15, 12, 8, 17, 8
)
hours_sleep = (
    7.0, 7.0, 6.0, 7.0, 7.0, 9.0, 6.0, 8.63, 6.0, 8.0, 7.0, 3.0, 6.0, 3.0, 6.0,
    3.0, 7.0, 8.0, 4.0, 0.0, 8.0, 6.0,
    6.0, 7.0, 6.5, 6.5, 8.0, 7.0, 7.0, 6.0, 5.0, 5.0, 6.0, 5.0, 9.0, 8.0, 10.0,
    5.0, 4.0, 7.0, 6.0, 7.0, 8.0, 6.0, 8.0,
    7.0, 7.0, 6.0, 6.0, 8.0, 7.0, 8.0, 6.0, 6.0, 8.0, 6.0, 6.0, 8.0, 7.0, 12.0,
    5.0, 7.5, 5.5, 7.0, 6.0, 6.5, 8.0, 8.0,
    6.0, 6.0, 8.0, 7.0, 5.0, 8.5
)


def mode(dataset):
    # mode
    frequency = {}

    for value in dataset:
        frequency[value] = frequency.get(value, 0) + 1

    most_frequent = max(frequency.values())

    mode = [key for key, value in frequency.items() if value ==
            most_frequent]
    return mode


def mean(dataset):
    mean = sum(dataset)/len(dataset)
    return mean


def main():
    dataset = input("Pick a dataset (siblings, credits, sleep): ")
    stats = input(
        "What stats do you wish to compute (min, max, mode, mean, all)? ")
    print(f"Dataset: {dataset}")

    if dataset.lower() == "siblings":
        if stats.lower() == "min":
            mi = min(num_siblings)
            print(f"Min: {mi}")
        elif stats.lower() == "max":
            ma = max(num_siblings)
            print(f"Max: {ma}")
        elif stats.lower() == "mode":
            mod = mode(num_siblings)
            print(f"Mode: {mod}")
        elif stats.lower() == "mean":
            # mean
            mea = mean(num_siblings)
            print(f"Mean: {mea}")
        elif stats.lower() == "all":
            print(f"Min: {min(num_siblings)}")
            print(f"Max: {max(num_siblings)}")
            print(f"Mode: {mode(num_siblings)}")
            print(f"Mean: {mean(num_siblings)}")

    if dataset.lower() == "credits":
        if stats.lower() == "min":
            mi = min(num_credits)
            print(f"Min: {mi}")
        elif stats.lower() == "max":
            ma = max(num_credits)
            print(f"Max: {ma}")
        elif stats.lower() == "mode":
            mod = mode(num_credits)
            print(f"Mode: {mod}")
        elif stats.lower() == "mean":
            # mean
            mea = mean(num_credits)
            print(f"Mean: {mea}")
        elif stats.lower() == "all":
            print(f"Min: {min(num_credits)}")
            print(f"Max: {max(num_credits)}")
            print(f"Mode: {mode(num_credits)}")
            print(f"Mean: {mean(num_credits)}")

    if dataset.lower() == "sleep":
        if stats.lower() == "min":
            mi = min(hours_sleep)
            print(f"Min: {mi}")
        elif stats.lower() == "max":
            ma = max(hours_sleep)
            print(f"Max: {ma}")
        elif stats.lower() == "mode":
            mod = mode(hours_sleep)
            print(f"Mode: {mod}")
        elif stats.lower() == "mean":
            # mean
            mea = mean(hours_sleep)
            print(f"Mean: {mea}")
        elif stats.lower() == "all":
            print(f"Min: {min(hours_sleep)}")
            print(f"Max: {max(hours_sleep)}")
            print(f"Mode: {mode(hours_sleep)}")
            print(f"Mean: {mean(hours_sleep)}")


main()
