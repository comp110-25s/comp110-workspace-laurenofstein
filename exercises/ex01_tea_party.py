"""To figure out the cost of a tea party for x amount of people"""

__author__: str = "730710469"


def main_planner(guests: int) -> None:
    """this functions tells us all the amounts of treats, and tea bags and also tells us the cost of everything"""
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(
        f"Cost: ${cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))}"
    )


def tea_bags(people: int) -> int:
    """this function tells us the amount of tea bags needed pe person"""
    return people * 2


def treats(people: int) -> int:
    """this functions tells us the amount of treats per person"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """this function tells you how much the tea party will costs including treats and tea bags"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))

def return_cost(tea_count: int, treat_count: int) -> float
    main_planner(guests=6.0) + (treat_count=9.0)
""""this function tells us the total amount of guests, cost, and product we will need to set up a tea party"""

return treats + cost
