def foobar(min, max):
    for i in range(min, max+1):
        square = i**.5
        prime = True
        for j in range(2, int(square)+1):
            if i%j == 0:
                prime = False
                break
        if prime:
            print i, "  Foo"
        elif square == round(square):
            print i, "  Bar"
        else:
            print i, "  FooBar"

foobar(100, 1000000)