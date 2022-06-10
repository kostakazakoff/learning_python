tribonacci_sequence = []
for _ in range(3):
    tribonacci_sequence.append(int(input()))
tribonacci_number = tribonacci_sequence[0]
spiral_number = int(input())
spiral_group = [spiral_number]
spiral_step = int(input())
spiral_row_len = 2
spiral_edge_numbers = []
edge_step = 1
equal = tribonacci_number == spiral_number
equal_number = [spiral_number]
range_of_numbers = range(1, 1000001)

while not equal:
    tribonacci_number = tribonacci_sequence[-1] + tribonacci_sequence[-2] + tribonacci_sequence[-3]
    tribonacci_sequence.append(tribonacci_number)

    for _ in range(spiral_row_len):
        spiral_number += spiral_step
        spiral_group.append(spiral_number)

    if (spiral_number or tribonacci_number) not in range_of_numbers:
        print('No')
        break

    spiral_edge_numbers += spiral_group[edge_step - 1:len(spiral_group):edge_step]
    equal_number = set(spiral_edge_numbers) & set(tribonacci_sequence)
    if equal_number:
        equal = True

    edge_step += 1
    spiral_group.clear()
    spiral_row_len += 2
else:
    print(*equal_number)




