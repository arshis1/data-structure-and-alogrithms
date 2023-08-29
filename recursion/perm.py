input_alphabets = ['a','b','c','d','e']
answer = []

for i in range(len(input_alphabets)):
    for j in range(len((input_alphabets))):
        if i!=j:
            for k in range(len(input_alphabets)):
                if k!=j and k!=i:
                    for l in range(len(input_alphabets)):
                        if l!=k and l!=j and l!=i:
                            output = input_alphabets[i] + input_alphabets[j] + input_alphabets[k] + input_alphabets[l]
                            if output in answer:
                                continue
                            else:
                                answer.append(output)

print(answer)






