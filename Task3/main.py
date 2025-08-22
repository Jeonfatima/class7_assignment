from my_agents.agent import Bot_agent
from agents import Runner,InputGuardrailTripwireTriggered
from Tools.tools import ORDER_DB
import asyncio


FAQS = {
    "hours": "Our store is open 9 AM – 9 PM, Monday to Saturday.",
    "shipping": "We offer free shipping on orders over $50.",
    "return": "You can return products within 30 days of delivery.",
    "payment": "We accept Visa, MasterCard, PayPal, and Apple Pay.",
    "international": "Yes, we ship internationally. Duties/taxes may apply."
}

async def main():

   try:
    prompt = input("Hi! How may i help you? ")
    result = await Runner.run(
        starting_agent=Bot_agent,
        input=prompt,
       context={"faqs": FAQS, "orders": ORDER_DB}
    )
    print(result.final_output)
   except InputGuardrailTripwireTriggered as ex:
     print("ERROR: " ,ex)

asyncio.run(main())