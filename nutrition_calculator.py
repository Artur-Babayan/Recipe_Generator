import openai
import json
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import os

load_dotenv()

class NutritionCalculator:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def calculate_nutritional_values(self, recipe_json: Dict[str, Any]) -> Optional[Dict[str, int]]:
        nutritional_prompt = f"""You are a food technologist. The recipe is provided between <recipe> and </recipe>.
        Calculate the total weight of the dish, the number of servings, and its nutritional values (calories, protein, fat, carbohydrates).
        Your output should be in JSON format defined between <format> and </format>. Do not ask any questions, just return the JSON with nutritional values.
        <format>
        {{
            "calories": [int],
            "protein": [int],
            "fat": [int],
            "carbohydrates": [int],
            "totalWeight": [int]
        }}
        </format>
        <recipe>
            {json.dumps(recipe_json)}
        </recipe>"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a food technologist."},
                {"role": "user", "content": nutritional_prompt}
            ],
            max_tokens=200
        )

        response_text = response['choices'][0]['message']['content']

        try:
            return json.loads(response_text)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    def __str__(self) -> str:
        return f"NutritionCalculator using OpenAI API Key: {os.getenv('OPENAI_API_KEY', 'Not Set')}"
