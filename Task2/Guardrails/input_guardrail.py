from agents import input_guardrail,RunContextWrapper,Agent,GuardrailFunctionOutput,Runner
from my_config.my_config import my_model
from pydantic import BaseModel
class MathOutPut(BaseModel):
    is_math: bool
    reason: str

@input_guardrail
async def check_input(
    ctx: RunContextWrapper, agent: Agent, input_data: str
) -> GuardrailFunctionOutput:
    # print("input_data : ", input_data)

    input_agent = Agent(
        "InputGuardrailAgent",
        instructions="Check and verify if input is related to math",
        model=my_model,
        output_type=MathOutPut,
    )
    result = await Runner.run(input_agent, input_data, context=ctx.context)
    final_output = result.final_output
    # print(final_output)

    return GuardrailFunctionOutput(
        output_info=final_output, tripwire_triggered=not final_output.is_math
    )