from agents import Agent
from my_config.my_config import  my_model
from pydantic import BaseModel

class MyDataType(BaseModel):
    is_query_about_hotel: bool
    reason: str

guardrial_agent = Agent(
    name="Guradrial Agent for Hotel Sannata",
    instructions="Check queries for hotel sannata",
    model=my_model,
    output_type=MyDataType

)