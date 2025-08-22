from agents import input_guardrail,GuardrailFunctionOutput,RunContextWrapper,Agent,Runner
from pydantic import BaseModel
from configuration.my_config import my_model

class MyDataType(BaseModel):
    is_offensive : bool
    reason : str

guardrail_agent = Agent(
    name="Input Guardrail Agent",
    instructions="You are an inout guardrail agent check fo any offensive or negative words in user prompt",
    model=my_model,
    output_type=MyDataType
)



@input_guardrail
async def input_guardrail(ctx:RunContextWrapper , agent:Agent , user_input:str) -> GuardrailFunctionOutput:

    result = await Runner.run(
        starting_agent=guardrail_agent,
        input=user_input
    )
    output = result.final_output
    return GuardrailFunctionOutput(
        output_info=output,
        tripwire_triggered = output.is_offensive
    )
