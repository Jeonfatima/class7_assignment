from agents import Runner, set_tracing_disabled,InputGuardrailTripwireTriggered
from my_agents.hotel_assistant import hotel_assistant

set_tracing_disabled(True)
hotels = {
    "Hotel Sannata": {
        "owner": "Mr. Ratan Lal",
        "total_rooms": 200,
        "private_rooms": 20
    },
    "Sunrise Inn": {
        "owner": "Ms. Sara Khan",
        "total_rooms": 150,
        "private_rooms": 10
    },
    "Ocean View": {
        "owner": "Mr. John Smith",
        "total_rooms": 180,
        "private_rooms": 15
    }
}

try:
    user_input = input("Whta is your query?")
    res = Runner.run_sync(
        starting_agent=hotel_assistant, 
        input=user_input,
        context={"hotels": hotels}
    )

    print(res.final_output)
except InputGuardrailTripwireTriggered as e:
    print(e)