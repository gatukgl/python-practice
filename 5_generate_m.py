generated_m = ""
total_block = 9
half_block = int(9 / 2)

for i in range(0, total_block):
    for j in range(0, total_block):
        if j == 0 or j == total_block - 1:
            generated_m += "*"
        elif (j == i or j == total_block - i - 1) and i < half_block:
            generated_m += "*"
        else:
            generated_m += " "

    generated_m += "\n"

print(generated_m) 
