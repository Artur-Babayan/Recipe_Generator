
# Recipe Generator & Nutrition Calculator

This project provides a Python application that interacts with OpenAI's GPT-4 API to generate meal recipes based on user input and calculate their nutritional values. It is structured using classes for better modularity and readability.

## Features

- **Recipe Generation**: Generates meal recipes using OpenAI's GPT-4 API based on parameters such as number of persons, dish type, dietary restrictions, cuisine, etc.
- **Nutritional Value Calculation**: Calculates nutritional values (calories, protein, fat, carbohydrates, total weight) for the generated recipe.
- **Modular Design**: The project is split into three main components:
  - `RecipeGenerator`: Handles recipe generation using the OpenAI API.
  - `NutritionCalculator`: Calculates nutritional values of the generated recipes.
  - `RecipeManager`: Manages the entire flow, including attaching nutritional values to the recipe.

## Project Structure

```
.
├── recipe_generator.py        # Handles generation of the recipe via OpenAI
├── nutrition_calculator.py     # Handles nutritional value calculations via OpenAI
├── recipe_manager.py           # Manages the flow between recipe generation and nutritional calculations
├── main.py                     # Main entry point for the application
├── .env                        # Stores the OpenAI API key
├── README.md                   # Documentation of the project
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Artur-Babayan/Recipe_Generator.git
   cd recipe-generator
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Set up your OpenAI API key:

   Create a file named `.env` in the root of your project with the following content:

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

   Replace `your_openai_api_key` with your actual OpenAI API key.

5. Run the application:

   ```bash
   python3 main.py
   ```

## Usage

You can customize the following parameters in the `main.py` file to generate your desired recipe:

- `amount_of_persons`: Number of people for whom the recipe is generated.
- `dish_type`: Type of dish (e.g., "salad", "soup").
- `max_cooking_time`: Maximum cooking time in minutes.
- `allergie_list`: A list of allergies to avoid (e.g., "nuts", "gluten").
- `diet_requirements`: A list of diet requirements (e.g., "vegan", "vegetarian").
- `cuisine_list`: Preferred cuisine (e.g., "Italian", "Mexican").
- `output_data_format`: Specifies the format of the generated recipe in JSON format.

## Example

```bash
python3 main.py
```

Sample output for a vegan salad:

```json
{
  "Name": "Vegan Caesar Salad",
  "CookingTime": "15 minutes",
  "RequiredTools": ["blender", "knife"],
  "Ingredients": [
    {"Name": "Romaine lettuce", "grams": 150},
    {"Name": "Cherry tomatoes", "grams": 100},
    {"Name": "Garlic", "piece": 1},
    {"Name": "Salt", "teaspoons": 1},
    {"Name": "Olive oil", "ml": 50},
    {"Name": "Lemon juice", "ml": 20},
    {"Name": "Parsley", "grams": 30},
    {"Name": "Vegan Parmesan cheese", "grams": 50}
  ],
  "Step-by-step directions": [
    "1. Tear the romaine lettuce into bite-size pieces.",
    "2. Cut the cherry tomatoes in half.",
    "3. Crush the garlic and mix with olive oil, lemon juice, salt, and parsley.",
    "4. Toss the salad with the dressing and top with vegan Parmesan."
  ],
  "nutritional_values": {
    "calories": 200,
    "protein": 5,
    "fat": 15,
    "carbohydrates": 10,
    "totalWeight": 450
  }
}
```

## Dependencies

- `openai`: Python client for OpenAI API.
- `python-dotenv`: For loading environment variables from `.env` file.
- `json`: Standard Python library for handling JSON data.
- `typing`: Standard Python library for type hinting.

Install all dependencies with:

```bash
pip3 install openai python-dotenv
```


