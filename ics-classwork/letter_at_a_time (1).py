# The code breaks unless your word is 7 characters long. If it was a list, then you'd see the letters listed from 0 to 6.
# The number would be 4. 0,1,2,3,4.
# 3. The index position would be 2.

message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in (list(range(7))):
    print(f"\t{i} - '{message[i]}'")

vowel_count = 0
for i in range(len(message)):
    letter = message[i].lower()
    if letter == "A" or "a" or "E" or "e" or "I" or "i" or "O" or "o" or "U" or "u":
        vowel_count += 1

print(f"\nYour message contains {vowel_count} vowels.")