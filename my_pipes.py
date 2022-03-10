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

########################################################################

count = Pipe(lambda iterable: len(iterable))
list_take = Pipe(lambda iterable, idx: iterable[:idx])
list_drop = Pipe(lambda iterable, idx: iterable[idx:])

resp2 = (
    [1,2,3]
    | list_take(2)
    | list_drop(1)
)

########################################################################

def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)

# fact_nums = [factorial(x) for x in range(1, 1000)] # ERROR!
fact_nums = (factorial(x) for x in range(1, 1000))

def fact():
    N = 100000
    a = 1
    for x in range(1, N + 1):
        a *= x
        yield a

# first_1000 = fact | list_take # ERROR!

########################################################################

@Pipe
def take(iterable, size):
    for item in iterable:
        if size > 0:
            size -= 1
            yield item
        else:
            return

fact_nums_2 = fact() | take(1000)

########################################################################

def counting():
    i = 0
    while True:
        i += 1
        yield i

@Pipe
def my_map(iterable, func):
    return map(func, iterable)

@Pipe
def to_list(iterable):
    return list(iterable)

def num_to_fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

fizzbuzz = counting() | my_map(num_to_fizzbuzz)
