# Casar ciphers dont exist, so I made a Caesar cipher instead.
print("mopline caesar cipher")
print("please all lowercase")
do = input("encode or decode? ")
what = input("what? ")
hm = int(input("whats the key "))
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
out = ""
if do == "encode":
    for x in range(len(what)):
        l = what[x]
        h = letters.index(l)+hm
        if h > len(letters):
            h-=len(letters)
        s = letters[h]
        out+=s
else:
    for x in range(len(what)):
        l = what[x]
        h = letters.index(l)-hm
        if h < 0:
            h+=len(letters)
        s = letters[h]
        out+=s
print(out)