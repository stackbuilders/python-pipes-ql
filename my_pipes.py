class Pipe:
    def __init__(self, fun):
        self.fun = fun

    def __ror__(self, arg):
        return self.fun(arg)

    def __call__(self, *args, **kwargs):
        return Pipe(lambda x: self.fun(x, *args, **kwargs))

########################################################################

# Creates pipes like the infix operator in Elm: (|>)
#
# arg
# |> fun1
# |> fun2
# |> fun3

########################################################################

identity = Pipe(lambda x: x)
exp = Pipe(lambda x, y: x ** y)

resp = (
    3
    | identity
    | identity
    | exp(3)
    | exp(2)
    | identity
    | exp(1/2)
    )
