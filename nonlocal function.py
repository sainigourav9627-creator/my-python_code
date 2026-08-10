nonlocal क्या करता है?
nonlocal का इस्तेमाल nested function में outer function के variable को बदलने के लिए होता है।

याद रखने की Trick

local        → current function का variable
global       → पूरे program का बाहर वाला variable
nonlocal    → outer function का variable 🔄


def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()
