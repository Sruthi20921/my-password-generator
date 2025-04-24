import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=?><[]{}'
length = int(input("Enter password length (min 4): "))

if length >= 4:
    password = ''.join(random.sample(chars, length))
    print("Password:", password)
    f = open("simple_passwords.txt", "a")
    f.write(password + "\n")
    f.close()
else:
    print("Too short!")
