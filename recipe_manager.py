from recipe_generator import RecipeGenerator
from nutrition_calculator import NutritionCalculator
import json
from typing import Optional, Dict, Any


class RecipeManager:
    def __init__(self):
        self.recipe_generator = RecipeGenerator()
        self.nutrition_calculator = NutritionCalculator()

    def attach_nutritional_values_to_recipe(self, recipe: Dict[str, Any], nutritional_values: Dict[str, int]) -> Dict[str, Any]:
        recipe['nutritional_values'] = nutritional_values
        return recipe

    def generate_full_recipe(self, amount_of_persons: int, dish_type: str, max_cooking_time: int,
                             allergie_list: list[str],
                             diet_requirements: list[str], cuisine_list: str, output_data_format: str) -> Optional[Dict[str, Any]]:
        prompt = self.recipe_generator.generate_recipe_prompt(amount_of_persons, dish_type, max_cooking_time,
                                                              allergie_list, diet_requirements, cuisine_list,
                                                              output_data_format)

        recipe = self.recipe_generator.get_recipe_from_openai(prompt)
        if recipe is None:
            print("Failed to parse recipe. Please check the OpenAI response.")
            return None

        nutritional_values = self.nutrition_calculator.calculate_nutritional_values(recipe)
        if nutritional_values is None:
            print("Failed to calculate nutritional values. Please check the OpenAI response.")
            return None

        full_recipe = self.attach_nutritional_values_to_recipe(recipe, nutritional_values)
        return full_recipe

    def __str__(self) -> str:
        return f"RecipeManager with RecipeGenerator: {self.recipe_generator} and NutritionCalculator: {self.nutrition_calculator}"
