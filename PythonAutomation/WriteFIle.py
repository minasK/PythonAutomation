file = open(r'C:\Users\minas\OneDrive\Desktop\PassTest.txt', 'r')
PassFile = open('PassFile.txt', 'w')
FailFile = open('FailFile.txt', 'w')
for line in file:
    line_split = line.split()
    if line_split[3] == 'P':
        PassFile.write(line)
    else:
        line_split[3] == 'F'
        FailFile.write(line)
file.close()
PassFile.close()
FailFile.close()