def generate_combinations(arr, k):
    if k == 0:
        yield []
    elif k == len(arr):
        yield arr
    else:
        for i in range(len(arr)):
            element = arr[i]
            remaining = arr[i+1:]
            for comb in generate_combinations(remaining, k-1):
                yield [element] + comb


def find_best_stops(stops, max_distance, rest_distance):
    best_combination = None
    min_stops = float('inf')

    for k in range(len(stops)):
        for comb in generate_combinations(stops, k+1):
            valid_comb = True
            for i in range(len(comb) - 1):
                if comb[i+1] - comb[i] < rest_distance:
                    valid_comb = False
                    break
            if valid_comb:
                if len(comb) < min_stops:
                    min_stops = len(comb)
                    best_combination = comb

    return best_combination


warung_stops = [10, 25, 30, 40, 50, 75, 80, 110, 130]
max_distance = 140
rest_distance = 30

best_stops = find_best_stops(warung_stops, max_distance, rest_distance)

if best_stops is None:
    print("Tidak ada solusi yang memenuhi persyaratan.")
else:
    print("Titik-titik warung yang harus Tono singgahi:")
    print(best_stops)
