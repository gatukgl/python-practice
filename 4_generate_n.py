generated_n = ""
total_block = 8

for i in range(0, total_block):
    for j in range(0, total_block):
        if j == 0 or j == total_block - 1:
            generated_n += "*"
        elif j == i:
            generated_n += "*"
        else:
            generated_n += " "

    generated_n += "\n"

print(generated_n) 
