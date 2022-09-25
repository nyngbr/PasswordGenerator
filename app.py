import random

passlen = int(input("enter the length of the password"))

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

p = "".join(random.sample(s,passlen))

print(p)

#nyngbr