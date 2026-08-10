return vs yield

return → function ko poori tarah stop कर देता है।
def test():
    return 1
    return 2

Sirf 1 milega।


yield → value deta hai aur function ko pause karta hai।

def test():
    yield 1
    yield 2

Dono values mil sakti hain।


सबसे आसान Trick

return = value do + function finish
yield = value do + pause + baad mein continue

Generator ka main benefit hai ki bahut saari values ko ek saath memory mein rakhne ke bajay ek-ek karke produce kar sakta hai.
Abhi bas Generator + yield ka basic concept samjho. Iske baad next() se dekhenge ki generator kaise step-by-step chalta hai.
