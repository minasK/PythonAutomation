# if we export it inside python then just put the file.txt
file = open(r'C:\Users\minas\OneDrive\Desktop\PassTest.txt', 'r')
for line in file:
    line_split = line.split()
    if line_split[3] == 'P':
        print(line)
file.close()