# function to find duplicates and to keep a count
def find_repetition(z):
    length = len(set(z))
    print(length)
    repeat = []               #for the number of duplicates
    outputs = []              #for a set of inputs

    for k in z:
        if z.count(k)>1:
            if k not in outputs:             #words are not repeated
                repeat.append(z.count(k))
                outputs.append(k)
                
        else :
            repeat.append(1)
            outputs.append(k)
    print(*repeat , sep = ' ')
    dictionary = dict(zip(outputs, repeat))
    dictionary_sorted = sorted(dictionary, key=dictionary.get, reverse=True)
    print("\nSorted: ")
    print(*dictionary_sorted, sep=' ')
    new_dict = {}
    for key, value in dictionary.items():
        if value in new_dict:
            new_dict[value].append(key) #if key already exists,appending new value
        else:
            new_dict[value]=[key] #adding a new key value pair
    max_num = max(repeat)
    min_num = min(repeat)
    print("\nMost repeated word: ")
    print(*new_dict.get(max_num), sep = ' ')
    print("\nLeast repeated word: ")
    print(*new_dict.get(min_num), sep = ' ')
    
# start of main function
num = int(input("Number of words:")) #number input from user 

inputs = []
i = 1
while i <= num:               
    a = input(f"Enter word {i}:")  #words input from user
    b = a.lower()                 #case sensitivity
    inputs.append(b)
    i += 1

find_repetition(inputs)  #calling function find_repetition
