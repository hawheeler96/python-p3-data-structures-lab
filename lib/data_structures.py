from venv import create


spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names


def get_spiciest_foods(spicy_foods):
    spiciest_foods_list = [food for food in spicy_foods if food.get("heat_level") > 5]
    return spiciest_foods_list


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name")
        cuisine = food.get("cuisine")
        heat_level = food.get("heat_level")

        print_peppers = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {print_peppers}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        list_cuisine = food.get("cuisine")

        if list_cuisine == cuisine:
            return food


get_spicy_food_by_cuisine(spicy_foods, "Thai")


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name")
        cuisine = food.get("cuisine")
        heat_level = food.get("heat_level")

        print_peppers = "🌶" * heat_level
        if heat_level > 5:
            print(f"{name} ({cuisine}) | Heat Level: {print_peppers}")


def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_spicy_foods = len(spicy_foods)
    
    for food in spicy_foods:
        total_heat_level += food.get("heat_level")
        
    avg_heat = total_heat_level / num_spicy_foods
    return avg_heat
        


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods_copy = spicy_foods.copy()
    spicy_foods_copy.append(spicy_food)
    return spicy_foods_copy

create_spicy_food(spicy_foods, {"name": "Griot", "cuisine": "Haitian", "heat_level": 10})
