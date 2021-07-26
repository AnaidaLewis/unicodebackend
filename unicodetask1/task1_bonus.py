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

    mx_num = max(repeat)
    v = repeat.index(mx_num)
    mx_word = outputs[v] 

    mn_num = min(repeat)
    u = repeat.index(mn_num)
    mn_word = outputs[u]

    return repeat , mx_num, mx_word, mn_num, mn_word


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
repeat = y[0]
mx_num = y[1]
mx_word = y[2]
mn_num = y[3]
mn_word = y[4]

print(*repeat , sep = ' ')

print(f"Most reapeated word is '{mx_word}', it is repeated '{mx_num}' times ")
print(f"Least reapeated word is '{mn_word}', it is repeated '{mn_num}' times ")