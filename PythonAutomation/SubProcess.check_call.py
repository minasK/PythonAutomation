import subprocess
# see the path that says Python, Python311 which is the path "C:\Users\minas\AppData\Local\Programs\Python\Python311\Lib\subprocess.py". Also, it is case-insensitive

for i in range(0, 5):
    subprocess.check_call(['Python', 'hello.py'])
