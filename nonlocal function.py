nonlocal क्या करता है?
nonlocal का इस्तेमाल nested function में outer function के variable को बदलने के लिए होता है।


def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()
