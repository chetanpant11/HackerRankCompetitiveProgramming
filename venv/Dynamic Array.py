first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m= int(first_multiple_input[1])

list_of_sequence = []
for i in range(n):
    list_of_sequence.append([])

lastans = 0
for i in range(m):

    p, q, r = map(int, input().split())
    if p == 1:
        # Calculate the index.
        index = (q ^ lastans) % n
        list_of_sequence[index].append(r)

    elif p == 2:
        index = index = (q ^ lastans) % n
        element_index = r % len(list_of_sequence[index])
        value = list_of_sequence[index][element_index]
        lastans = value
        print(value)