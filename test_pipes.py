import pipe as p
from datetime import date

if __name__ == "__main__":
    """
        Sum all the even:
    """
    # Using pipes:
    res_pipes = sum(range(100) | p.where(lambda x: x % 2 == 0))
    print("Result", res_pipes)

    print("="*20)

    """
        All the fuel expenses of january
    """
    expenses = [
        { "category": "Fuel", "value": 10.50, "date": date(2022, 1, 3) },
        { "category": "Fuel", "value": 18.50, "date": date(2022, 1, 4) },
        { "category": "Food", "value": 48.34, "date": date(2022, 1, 5) },
        { "category": "Fuel", "value": 5.50, "date": date(2022, 1, 7) },
        { "category": "Clothes", "value": 101.50, "date": date(2022, 2, 1) },
    ]

    total_pipes = sum(
        expenses
        | p.where(lambda expense:
            expense["category"] == "Fuel" and expense["date"].month == 1
          )
        | p.select(lambda expense: expense["value"])
    )
    print("All expenses in JAN", total_pipes)

    print("="*20)

    """
        Sum the first 8 multiples of 5 in the factorial series
    """

    def fact():
        N = 100000
        a = 1
        for x in range(1, N + 1):
            a *= x
            yield a

    total = list(fact() | p.where(lambda n: n % 5 == 0) | p.take(8))
    print("Values", total)
    print("Total", sum(total))
