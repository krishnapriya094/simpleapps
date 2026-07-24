text = input("Enter a string: ")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("Reversed:", text[::-1])

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)