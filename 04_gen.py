def inner():
    print('dentro')
    value = yield 2
    print('Recebido', value)
    return 4


def outer():
    yield 1
    ret = yield from inner()
    print('retornou', ret)
    yield 5

# await delegar

# a task nunca tem controle
