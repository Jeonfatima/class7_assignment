from agents import OpenAIChatCompletionsModel , AsyncOpenAI
from decouple import config

api_key = config("GEMINI_API_KEY")
base_url = config("BASE_URL")

my_client = AsyncOpenAI(api_key=api_key , base_url=base_url)

my_model = OpenAIChatCompletionsModel(model="gemini-2.5-flash" , openai_client=my_client)