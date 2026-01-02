scores = [2, 45, 102, 4, 9, 12, 45, 90, 1, 0, 1]

n_min = int(scores[0]);
n_max = int(scores[0]);
n_sum = 0
for score in scores:
    n_sum += score
    if n_min > score:
        n_min = score
    if n_max < score:
        n_max = score

print(f"The minimum score is {n_min} and the maximum score is {n_max} and total score is {n_sum}")


total = sum(scores)
print(f"The total score is {total}")