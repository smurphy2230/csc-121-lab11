#  ask user to enter a string, convert to uppercase. store results in dictionary
user_input = input("Enter a string of your choice: ").upper()
letters = []
counts = []
for i in user_input:
    if i.isalpha():
        if i not in letters:
            num = user_input.count(i)
            letters.append(i)
            counts.append(num)

#  store letters and counts in dictionary
count_dict = {letters[i]: counts[i] for i in range(len(letters))}
print("Dictionary of letter counts: ", count_dict)
#  ask user to input a letter. check if in dictionary, if present display count and
#  delete from dictionary. display new dictionary after letter removed
letter = input("Please enter a letter: ").upper()
print("Letter chosen: ", letter)
if letter in count_dict:
    print("count of chosen letter: ", count_dict[letter])
    del count_dict[letter]
    print("New dict after letter removed: ", count_dict)
else:
    print("letter not found")

#  create a sorted list from dictionary letters and display it
sorted_list = list(count_dict.keys())
sorted_list.sort()
print(sorted_list)





