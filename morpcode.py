# Casar ciphers dont exist, so I made a Caesar cipher instead.
print("mopline caesar cipher")
print("please all lowercase")
do = input("encode or decode? ")
what = input("what? ")

def encode ( w , t ) :
    ei = 1
    i = 1
    words = []
    toencrypt = ""
    oi = 1
    wi = 1
    pso = []
    


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