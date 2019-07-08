strings_count = int(input())

strings = []

for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

queries_count = int(input())

queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

count=0
for i in range(len(queries)):
    count=0
    for j in range(len(strings)):
        if queries[i]==strings[j]:
            count=count+1
        else:
            continue

    print(count)