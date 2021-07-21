# function to find duplicates and to keep a count
def find_repetition(z):
    print(len(set(z)))
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
            
    return repeat


# start of main function
num = int(input("Number of words: ")) #number input from user 

inputs = []
i = 1
while i <= num:               
    a = input(f"Enter word {i}: ")  #words input from user
    b = a.lower()                 #case sensitivity
    inputs.append(b)
    i += 1


y = find_repetition(inputs)  #calling function find_repetition

print(*y, sep = ' ')
