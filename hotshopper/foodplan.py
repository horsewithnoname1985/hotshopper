from hotshopper.recipes import Recipe
from hotshopper.ingredients import piece, Supermarket, Market


class ShoppingList(list):

    def __contains__(self, type):
        for ingredient in self:
            if isinstance(ingredient, type):
                return True
            return False

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add(self, ingredient):
        for existing_ingredient in self:
            if isinstance(ingredient, type(existing_ingredient)):
                if ingredient.unit.specifier == piece.specifier:
                    existing_ingredient.amount_piece += ingredient.amount_piece
                else:
                    existing_ingredient.amount += ingredient.amount
                return True
        self.append(ingredient)

    def substract(self, ingredient):
        for existing_ingredient in self:
            if isinstance(ingredient, type(existing_ingredient)):
                if ingredient.unit.specifier == piece.specifier:
                    existing_ingredient.amount_piece -= ingredient.amount_piece
                else:
                    existing_ingredient.amount -= ingredient.amount
                if existing_ingredient.amount <= 0 \
                    & existing_ingredient.amount_piece <= 0:
                    self.remove(ingredient)


class FoodPlan:

    def __init__(self):
        self.recipes = []
        self.shopping_list_supermarket = ShoppingList()
        self.shopping_list_market_week1 = ShoppingList()
        self.shopping_list_market_week2 = ShoppingList()
        self.shopping_list_market_week3 = ShoppingList()

        self.shopping_list_supermarket.set_name("Supermarkt")
        self.shopping_list_market_week1.set_name("Markt Woche 1")
        self.shopping_list_market_week2.set_name("Markt Woche 2")
        self.shopping_list_market_week3.set_name("Markt Woche 3")

    def __add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)

        for ingredient in recipe.ingredients:
            if isinstance(ingredient.where, Supermarket):
                self.shopping_list_supermarket.add(ingredient)
            elif isinstance(ingredient.where, Market):
                if 1 in recipe.weeks:
                    self.shopping_list_market_week1.add(ingredient)
                if 2 in recipe.weeks:
                    self.shopping_list_market_week2.add(ingredient)
                if 3 in recipe.weeks:
                    self.shopping_list_market_week3.add(ingredient)

    def __remove_recipe(self, recipe: Recipe):
        self.recipes.remove(recipe)

        for ingredient in recipe.ingredients:
            if isinstance(ingredient.where, Supermarket):
                self.shopping_list_supermarket.substract(ingredient)
            elif isinstance(ingredient.where, Market):
                if 1 in recipe.weeks:
                    self.shopping_list_market_week1.substract(ingredient)
                if 2 in recipe.weeks:
                    self.shopping_list_market_week2.substract(ingredient)
                if 3 in recipe.weeks:
                    self.shopping_list_market_week3.substract(ingredient)

    def set_shopping_lists(self, recipes: list):
        for recipe in recipes:
            if recipe.selected:
                self.__add_recipe(recipe)

    def get_shopping_lists(self):
        return [self.shopping_list_supermarket,
                self.shopping_list_market_week1,
                self.shopping_list_market_week2,
                self.shopping_list_market_week3]
