import hashlib

flag = 0

pass_hash = input("MD5 Hash: ")

wordlist = input("File: ")

try:
    pass_file = open(wordlist, "r")
except:
    print("404: File Not Found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    print(word)
    print(digest)
    print(pass_hash)

    if digest == pass_hash:
        print("Password found")
        print(word)
        flag = 1
        break

if flag == 0:
    print("Password not in list.")
