import openai
import json
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import os

load_dotenv()

class RecipeGenerator:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def generate_recipe_prompt(self, amount_of_persons: int, dish_type: str, max_cooking_time: int, allergie_list: list[str],
                               diet_requirements: list[str], cuisine_list: str, output_data_format: str) -> str:
        prompt = f"""Hey, ChatGPT, generate me a meal recipe for {amount_of_persons} and {dish_type}
                    with cooking time under {max_cooking_time} minutes,
                    good for people with allergies to {allergie_list},
                    following {diet_requirements},
                    preferring the {cuisine_list} cuisine.
                    Your output should look like {output_data_format}, You are not asking questions,
                    just responding with recipe."""
        return prompt

    def get_recipe_from_openai(self, prompt: str) -> Optional[Dict[str, Any]]:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                    {"role": "system", "content": "You are an assistant that helps generate meal recipes."},
                    {"role": "user", "content": prompt}
                ],
            max_tokens=1000
        )

        recipe_response = response['choices'][0]['message']['content']

        try:
            return json.loads(recipe_response)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    def __str__(self) -> str:
        return f"RecipeGenerator using OpenAI API Key: {os.getenv('OPENAI_API_KEY', 'Not Set')}"
