from agents import Agent
from my_config.my_config import my_model
from Guardrails.input_guardrail import check_input
from Guardrails.output_guardrails import check_output

math_agent = Agent(
    "math Agent",
    instructions="You are a helpful agent",
    model=my_model,
    input_guardrails=[check_input],
    handoff_description="provide error input not related to math or else answer"
)


political_agent = Agent(
    "political Agent",
    instructions="You are a helpful agent",
    model=my_model,
    output_guardrails=[check_output],
    handoff_description="provide error id outut related to politics"
)

general_agent = Agent(
    name="General agent",
    instructions="you are a genral agent that answers only if inout is realted to math and handoff to math agent and if input or output related to politics hand off to politics agent and then return answer",
    model=my_model,
    handoffs=[math_agent,political_agent]

)