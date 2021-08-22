# send e um next com parametro  // uma pilha


def gen():
    print('comecando')
    a = yield

    print('primeiro', a)
    b = yield

    print('segundo', b)
    yield
    print('soma', a+b)
