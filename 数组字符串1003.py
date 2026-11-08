a,b,c = map(int, input().split())
people = list(range(a))
while len(people) > 1:
    b = (b + c - 1) % len(people)
    people.pop(b)
print(people[0])