"""

Quarantine has given you a chance to experiment with
multiple recipes and you have decided to create an app
for organizing all of your favourite recipes.

In this tutorial, we will implement a subset of the
functions needed for this app.

Complete 2 docstring examples and the function
body for each function below.

Function correctness - 80%
Docstring examples - 20%

---- IMPORTANT!!! ----
Do NOT call the print() or input() builtin functions.
Do NOT add any import statements.
Do NOT add any lines of code outside of function definitions.

You may create additional functions.
"""
import doctest


def get_recipes_lower_than_calorie_threshold(recipes, calories, threshold):

    """
    recipes: List of str
    calories: List of float
    threshold: float

    Returns List of str. recipes and calories are
    the recipes' names and calorie-content, respectively.
    Return all recipes whose calorie-content is strictly less
    than threshold.

    Precondition i.e., you can assume the following is true:
    * len(recipes) == len(calories)

    NOTE: use ... to split your docstring examples across multiple
    lines
    >>> recipes = [
    ... "chicken schnitzel", "lemonade", "spiced salmon"
    ... ]
    >>> calories = [2668.0, 834.0, 1096.0]
    >>> result = get_recipes_lower_than_calorie_threshold(
    ... recipes, calories, 2668.0
    ... )
    >>> result == ["lemonade", "spiced salmon"]
    True

    """
    result = []
    for i in range(len(calories)):
        if calories[i] < threshold:
            result.append(recipes[i])
    
    return result


def get_total_calories(
    recipe_ingredients,
    recipe_quantities,
    ingredients_names,
    ingredients_calories
    ):

    """
    recipe_ingredients: List of str
    recipe_quantities: List of float
    ingredients_names: List of str
    ingredients_calories: List of float

    Returns float; returns the total calories of the recipe whose ingredients
    are specified in recipe_ingredients and their corresponding quantities
    are specified in recipe_quantities.
    ingredients_names and ingredients_calories include a list of ingredients
    and their corresponding calories, respectively.

    For instance, if
    * recipe_ingredients is
    ["cup of lemon", "cup of water", "cup of sugar"]
    * recipe_quantities is [1.0, 3.0, 1.0]
    * ingredients_names is
    [
    "cup of water", "tbsp of sugar", "cup of lemon",
    "tsp of olive oil", "cup of sugar"
    ]
    * ingredients_calories is [0.0, 48.0, 61.0, 120.0, 773.0]
    Then the total number of calories is
    (1.0 * 61.0) + (3.0 * 0.0) + (1.0 * 773.0) = 834.0

    Precondition
    * len(recipe_ingredients) == len(recipe_quantities)
    * len(ingredients_names) == len(ingredients_calories)
    * all items in recipe_ingredients and ingredients_names
    include lower-case characters only.
    * all items in recipe_ingredients are also in ingredients_names

    NOTE: use ... to split your docstring examples across multiple
    lines
    >>> recipe_ingredients = ["cup of lemon", "cup of water", "cup of sugar"]
    >>> recipe_quantities = [1.0, 3.0, 1.0]  
    >>> ingredients_names = [
    ... "cup of water", "tbsp of sugar", "cup of lemon",
    ... "tsp of olive oil", "cup of sugar"
    ... ]
    >>> ingredients_calories = [0.0, 48.0, 61.0, 120.0, 773.0]
    >>> total = (1.0 * 61.0) + (3.0 * 0.0) + (1.0 * 773.0)
    >>> total == 834.0
    True

    """
    result = 0.0
    for i in range(len(recipe_ingredients)):
        for j in range(len(ingredients_names)):
            if recipe_ingredients[i] == ingredients_names[j]:
                result += recipe_quantities[i] * ingredients_calories[j]
    return result
    


def get_low_cal_recipes(
    recipes,
    recipes_ingredients,
    recipes_quantities,
    ingredients_names,
    ingredients_calories
    ):

    """
    recipes: List of str
    recipes_ingredients: List of List of str
    recipes_quantities: List of List of float
    ingredients_names: List of str
    ingredients_calories: List of float

    Returns List of str; returns a list of recipe names, whose total
    calorie content is less than 700.0.
    recipes is a list of recipe names.
    recipes_ingredients and recipes_quantities are both nested lists that contain
    the ingredients and quantities required for each of the recipes, respectively

    i.e., recipes_quantities[i][j] is the quantity
    required of the ingredient recipes_ingredients[i][j]
    to make the recipe recipes[i], where the index j represents the
    jth ingredient of the ith recipe.

    Hint: use the functions:
    * get_total_calories
    * get_recipes_lower_than_calorie_threshold

    Preconditions:
    * len(recipes) == len(recipes_ingredients) == len(recipes_quantities)
    * len(recipes_ingredients[i]) == len(recipes_quantities[i])
    * len(ingredients_names) == len(ingredients_calories)
    * all strings in recipes, recipes_ingredients and ingredients_names
    include lower-case characters only
    * all ingredients in recipes_ingredients are also in ingredients_names

    """
            

    pass


if __name__ == "__main__":
    # uncomment the line below to run your doctest
    # DO NOT REMOVE INDENTATION
    doctest.testmod()

    # comment this out when running your doctests
    pass
