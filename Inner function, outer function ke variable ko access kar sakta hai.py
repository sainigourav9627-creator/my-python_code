def outer(name):
    print("hello")
    def inner():
        print("hello",name)
    inner()
outer("gourav")
