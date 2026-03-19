# Create a list of 5+ numbers
number_list = [1, 2, 3, 4, 5, 6]
number_list.append(69)
print(number_list)  ## [1, 2, 3, 4, 5, 6, 69]

number_list.pop(-1)
print(number_list)  ## [1, 2, 3, 4, 5, 6]

# Sum all numbers in list, count numbers in list, find average
sum = 0
average = 0
list_count = 0

for number in number_list:
    sum += number
    list_count += 1

average = sum / list_count

print(sum)  ## 21
print(list_count)  ## 6
print((f"{average:.2f}"))  ## 3.5


# Sum all even numbers in list

even_sum = 0
odd_sum = 0

for number in number_list:
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

print(even_sum)  ## 12
print(odd_sum)  ## 9

# Slice first 3
print(number_list[:3])  ## [1, 2, 3]

# Slice last 2
print(number_list[-2:])  ## [5, 6]
# Slice evevery second element
print(number_list[::2])  ## [1, 3, 5]
