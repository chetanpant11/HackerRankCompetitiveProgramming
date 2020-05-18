"""nm = input().split()

n = int(nm[0])

m = int(nm[1])

topic = []

for _ in range(n):
    topic_item = input()
    topic.append(topic_item)
a=0
con=[]
for i in range(0, n-1):
    for j in range(i+1, n):
        count=0
        for k in range(0, m):
            if topic[i][k]=="1" or topic[j][k]=="1":
                count+=1
        con.append(count)

e=max(con)
print(e)
f=con.count(e)
print(f)"""
# !/bin/python3

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    persons = []
    for _ in range(n):
        person = str(input().strip())
        persons.append(person)
    size = len(persons)
    max_topics_numbers = 0
    teams = 0
    for i in range(0, size):
        for j in range(i + 1, size):
            topics = str("{0:b}".format((int(persons[i], 2) | int(persons[j], 2))))
            if topics.count("1") > max_topics_numbers:
                max_topics_numbers = topics.count("1")
                teams = 1
            else:
                if topics.count("1") == max_topics_numbers:
                    teams += 1
    print(max_topics_numbers)
    print(teams)
