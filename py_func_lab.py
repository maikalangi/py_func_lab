# Exercise 1
def sum_to(n):
    sum = list(range(n+1))
    i = 0
    for num in sum:
        i = i + num
    print(i)

sum_to(8)
# >36

# Exercise 2
def largest(list):
    new = 0
    for num in list:
        if num > new:
            new = num
    print(new)

scroll = [54, 23, 7, 108, 46, 1]
largest(scroll)
# >108

# Exercise 3
def occurances(string1, string2):
    sum = 0
    for letter in string1:
        if string2 == letter:
            sum = sum + 1
    print(sum)

occurances('supercalifragilisticexpialidocious', 'i')
# >7

# Exercise 4
def product(*arbitrary):
    prod = list(arbitrary)
    group = 1
    for num in prod:
        group = group * num
    print(group)


product(1, 2, 4, 5, 3)
# >120