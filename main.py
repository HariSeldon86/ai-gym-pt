from dotenv import load_dotenv
load_dotenv(".env") # for run using .env file

from rich import print
import json

from models import Workout

if __name__ == "__main__":

    from langchain.chat_models import init_chat_model

    # Ensure you have set the required environment variable for init_chat_model
    model = init_chat_model(
        model="google_genai:gemini-2.5-flash-lite",  # or another model e.g. openai:gpt-5-nano, google_genai:gemini-2.5-flash-lite
        temperature=0.0,
    )

    model_structured = model.with_structured_output(Workout)
    model_structured_raw = model.with_structured_output(Workout, include_raw=True)

    query = """
Create a workout plan with the following parameters:
- Goal: Muscle Gain
- Equipment: all gym equipments
- Days per week: 3
- Exercise per day: 5
- Preference: I don't want barbell exercises
Provide sets, reps, and rest time for each exercise.
"""
    if False:
        # Return both structured data and raw response
        response = model_structured_raw.invoke(query)
        workout = response["parsed"]

    else:
        # Return only structured data as pydantic model Workout
        workout = model_structured.invoke(query)

    print(workout)
    data = workout.model_dump()  # type: ignore

    # Save the workout plan to a JSON file
    with open("workout_plan.json", "w") as f:
        json.dump(data, f, indent=2)

    from toon import encode

    # Encode the workout plan to a Toon file
    toon_data = encode(data)
    with open("workout_plan.toon", "w") as f:
        f.write(toon_data)
