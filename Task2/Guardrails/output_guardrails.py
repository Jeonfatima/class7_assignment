from agents import output_guardrail,RunContextWrapper,Agent,GuardrailFunctionOutput,Runner
from my_config.my_config import my_model
from pydantic import BaseModel
class PoliticalOutPut(BaseModel):
    is_political: bool
    reason: str

@output_guardrail
async def check_output(
    ctx: RunContextWrapper, agent: Agent, output_data: str
) -> GuardrailFunctionOutput:
   

    output_agent = Agent(
        "InputGuardrailAgent",
        instructions="Check and verify if output is related political topics and references to political figures.",
        model=my_model,
        output_type=PoliticalOutPut,
    )
    result = await Runner.run(output_agent, output_data, context=ctx.context)
    final_output = result.final_output
    # print(final_output)

    return GuardrailFunctionOutput(
        output_info=final_output, tripwire_triggered= final_output.is_political
    )