import os 
from dotenv import load_dotenv
import typing_extensions as typing
import google.generativeai as genai



load_dotenv()


API_KEY = os.getenv("API_KEY")


genai.configure(api_key=API_KEY)



class Recipe(typing.TypedDict):
    recipe_name: str
    ingredients: list[str]

model = genai.GenerativeModel("gemini-1.5-pro-latest")
result = model.generate_content(
    "List a few popular cookie recipes.",
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json", response_schema=list[Recipe]
    ),
)
print(result)
