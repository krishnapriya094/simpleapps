numbers = [45, 12, 89, 23, 7, 56]

print("Original List:", numbers)

numbers.sort()
print("Ascending Order:", numbers)

numbers.sort(reverse=True)
print("Descending Order:", numbers)

print("Smallest number:", min(numbers))
print("Largest number:", max(numbers))