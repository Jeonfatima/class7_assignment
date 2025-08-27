from agents import Runner,InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered
from my_agents.agent import general_agent
import asyncio

async def main():
   try:
       user_input = input("What is your question :")
       result = await Runner.run(
        starting_agent=general_agent,
        input=user_input,
        
         )
       print(result.final_output)
   except InputGuardrailTripwireTriggered as ex:
       print("Error ----> " ,ex)
   except OutputGuardrailTripwireTriggered as ex:
       print("Error ------> " , ex)

asyncio.run(main())