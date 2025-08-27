from agents import Agent,RunContextWrapper
from my_config.my_config import my_model
from guardrail.guardrail_input_function import guardrail_input_function


async def dynamic_instructions(ctx:RunContextWrapper,agent:Agent):
    return f"You are a helpful hotel assistant agent that helps the user regarding the query of the hote provided to you in context. Always start anwer by mentionaing all the hotel names {ctx.context["hotels"]} where necessary"
hotel_assistant = Agent(
    name="Hotel Customer care",
    instructions=dynamic_instructions,
    model=my_model,
    input_guardrails=[guardrail_input_function],
   
)