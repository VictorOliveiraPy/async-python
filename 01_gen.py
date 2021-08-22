# gerador
# so de acrescentar um yield na funcao ele virar um gerador
# quando um gerador retornar ele manda um StopIteration

def g():
    print('Opa!')
    yield 42
    print('Mais um')
    yield 'asdf'
    print('entrando...')
    for i in range(5):
        print('no loop', i)
        yield i
    print('final')

    return 123


if __name__ == '__main__':
    gen = g()
    try:
        while True:
            next(gen)
    except StopIteration as e:
        print(e.value)
