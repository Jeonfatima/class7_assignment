from agents import Agent,RunContextWrapper,ModelSettings
from configuration.my_config import my_model
from Tools.tools import get_order_status
from Guardrails.guardrails import input_guardrail

Human_agent = Agent(
    name="Human Agent",
    instructions="You are a human agent that acts as a handoff for bot agent when asked complicated questions that bot agnt have no context of ",
    model=my_model,
    model_settings=ModelSettings(
        tool_choice="none",
    ),
)

async def dynamic_instructions(ctx: RunContextWrapper, agent: Agent):
    faqs = ctx.context or {}
    return f"""
    You are a helpful support bot.

    FAQs you can use to answer:
    {faqs}

    You can also track order status using the tool `get_order_status`and answer like the return statement in that tool withput summarizing.
    If the user asks about an order status and the order ID is invalid or not found in the database, respond with:
'❌ Order ID not found. Please provide a valid order ID.'

Only if the query is unrelated to orders or cannot be handled by tools, then respond:
'A human agent will assist you shortly.'

    If the user asks something outside FAQs or orders, hand off to the human agent by saying
    'A human agent will assist you shortly.'
    """


Bot_agent = Agent(
    name="Bot Agent",
    instructions=dynamic_instructions,
    handoffs=[Human_agent],
    tools=[get_order_status],
    input_guardrails=[input_guardrail],
    model=my_model
)