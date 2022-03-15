from __future__ import annotations

from typing import Generic, TypeVar, Callable

Arg = TypeVar("Arg")

class Validator(Generic[Arg]):
    def __init__(self, fun: Callable[[Arg], bool]):
        self.fun = fun

    def __and__(self, other: Validator[Arg]) -> Validator[Arg]:
        return Validator(lambda x: self.fun(x) and other.fun(x))

    def __or__(self, other: Validator[Arg]) -> Validator[Arg]:
        return Validator(lambda x: self.fun(x) or other.fun(x))

    def validate(self, val: Arg) -> bool:
        return self.fun(val)

gt3 = Validator[int](lambda x: x > 3)
lt7 = Validator[int](lambda x: x < 7)
is0 = Validator[int](lambda x: x == 0)

@Validator
def isEven(num: int) -> bool:
    return num % 2 == 0

@Validator
def has_char_A(string: str) -> bool:
    return "A" in string

myValidator = gt3 & lt7 | is0 | isEven
# myValidator = lambda x: x > 3 and x < 7 or x == 0 or x % 2 == 0

print("5", myValidator.validate(5))
print("0", myValidator.validate(0))
print("1", myValidator.validate(1))
print("8", myValidator.validate(8))
