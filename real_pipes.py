print(50*"#")

class Pipe:
    def __init__(self, fun):
        self.fun = fun

    def __ror__(self, arg):
        return self.fun(arg)

    def __call__(self, *args, **kwargs):
        return Pipe(lambda x: self.fun(x, *args, **kwargs))

iddy = Pipe(lambda x: x)
exp = Pipe(lambda x, y: x ** y)
stdio = Pipe(lambda thing: print(thing))

# exp(3,iddy(iddy(3)))
result = (
  3
  | iddy
  | iddy
  | exp(2)
  | exp(2)
)

## Iterators & Iterables
select = Pipe(lambda iterable, selector: map(selector, iterable))
to_list = Pipe(lambda iterable: list(iterable))

result2 = (
    [1,2,3]
    | select(lambda x: x*3)
    | select(lambda x: x+3)
    | select(lambda x: x**3)
    | to_list
)

# print(result2)

## Generators
def ones():
    while True:
        yield 1

# print(next(ones()))
# print(next(ones()))
# print(next(ones()))

zeros = (
    ones()
    | select(lambda x: x - 1)
    )

# for zero in zeros:
#     print(zero)

## Decorators
@Pipe
def take(iterable, qte):
    for item in iterable:
        if qte > 0:
            qte -= 1
            yield item
        else:
            return

result3 = (
    ones()
    | select(lambda x: x + 3)
    | take(5)
    | to_list
)

## FizzBuzz
def counting():
    x = 1
    while True:
        yield x
        x += 1

def num_to_fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return str(n)

result4 = (
    counting()
    | take(1000)
    | select(num_to_fizzbuzz)
)

for v in result4:
    print(v)
