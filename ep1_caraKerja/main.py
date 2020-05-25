import time
start_time = time.time()

print("halodunia")
print("apa kabarnya")
print("baik banget")

a = 13
print(a) #ini adalah comment
"""ada apa ucup dengan
si ganteng dalam comment multiline"""
print(1+a)
for i in range(1, 1000):
    a = 10

print(time.time() - start_time, "detik")
#bisa compile python ke bytecode
#cara compile, terminal type
#python3 -m py_compile main.py