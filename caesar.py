# Casar ciphers dont exist, so I made a Caesar cipher instead.
print("mopline caesar cipher")
print("please all lowercase")
do = input("encode or decode? ")
what = input("what? ")
hm = int(input("whats the key "))
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
done = ""
def encode ( w , t ) :
    out = ""
    for x in range(len(w)):
        l = w[x]
        if letters.__contains__(l) :
            h = letters.index(l)+t
            if h > len(letters)-2:
                h-=len(letters)
            s = letters[h]
            out+=s
        else:
            out+=l
    return out
def decode ( w , t ) :
    out = ""
    for x in range(len(w)):
        l = w[x]
        if letters.__contains__(l) :
            h = letters.index(l)-t
            if h < 0:
                h+=len(letters)
            s = letters[h]
            out+=s
        else:
            out+=l
    return out
if do == "encode":
    done = encode(what, hm)
else:
    done = decode(what, hm)
print(done)