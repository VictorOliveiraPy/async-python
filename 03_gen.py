def double():
    v = 0
    while True:
        v += yield v * 2


def seq(n):
    d = double()
    next(d)
    for i in range(n):
        yield d.send(i)


g = seq(5)
