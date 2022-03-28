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

print("\nResult Pipes 1:",
  3
  | iddy
  | exp(2)
  | iddy
  | iddy
  | exp(2)
)

## Iterators & Iterables

select = Pipe(lambda iterable, selector: map(selector, iterable))
to_list = Pipe(lambda iterable: list(iterable))
add = Pipe(lambda iterable: sum(iterable))

class Range:
    def __init__(self, init, end):
        self.init = init
        self.end = end

    def __next__(self):
        aux = self.init
        if self.init <= self.end:
            self.init += 1
            return aux
        raise StopIteration()

    def __iter__(self):
        return self

print("\nResult Pipes 2:",
    Range(3, 7)
    | select(lambda x: x*3)
    | select(lambda x: x+3)
    | select(lambda x: x**3)
    | to_list
)

## Generators

def my_range(init, end):
    aux = init
    while aux <= end:
        yield aux
        aux += 1

print("\nResult Pipes 3:",
    my_range(3, 7)
    | select(lambda x: x*3)
    | select(lambda x: x+3)
    | select(lambda x: x**3)
    | to_list
)

## Decorators

@Pipe
def take(iterable, qte):
    for item in iterable:
        if qte > 0:
            qte -= 1
            yield item
        else:
            return

print("\nResult Pipes 4:",
    my_range(10, 100)
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

print("\nFizz Buzz:")

fizzbuzz = (
    counting()
    | take(10)
    | select(num_to_fizzbuzz)
)

for fb in fizzbuzz:
    print(fb)
