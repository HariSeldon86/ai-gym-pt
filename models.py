from pydantic import BaseModel, Field

from data_models import (
    ExerciseName,
    MuscleGroup,
    Equipment,
    Difficulty,
    Type,
    Goal,
)

class Exercise(BaseModel):
    """Base model for an exercise."""

    name: ExerciseName = Field(..., description="Name of the exercise")
    muscle_group: MuscleGroup = Field(..., description="Targeted muscle group")
    equipment: Equipment = Field(..., description="Equipment needed for the exercise")
    difficulty: Difficulty = Field(..., description="Difficulty level of the exercise")
    type: Type = Field(..., description="Type of exercise (e.g., strength, cardio)")


class WorkoutExercise(Exercise):
    """Model for a specific exercise in a workout with additional details."""

    sets: int = Field(..., description="Number of sets")
    reps: int = Field(..., description="Number of repetitions per set")
    rest_time: int = Field(..., description="Rest time between sets in seconds")
    order: int = Field(..., description="Order of the exercise in the workout")


class WorkoutDay(BaseModel):
    """Base model for a workout."""

    day: int = Field(..., description="Day number in the workout plan")
    exercises: list[WorkoutExercise] = Field(
        ..., description="List of exercises for the day"
    )


class Workout(BaseModel):
    """Model for a complete workout plan."""

    name: str = Field(..., description="Name of the workout plan")
    description: str = Field(..., description="Description of the workout plan")
    difficulty: Difficulty = Field(..., description="Overall difficulty level of the workout plan")
    goal: Goal = Field(..., description="Primary goal of the workout plan")
    duration_weeks: int = Field(..., description="Duration of the workout plan in weeks")
    days_per_week: int = Field(..., description="Number of workout days per week")
    workout_days: list[WorkoutDay] = Field(
        ..., description="List of workout days in the plan"
    )

    def model_dump(self, **kwargs):
        """Custom model dump to convert Enums to their values."""
        data = super().model_dump(**kwargs)
        for day in data["workout_days"]:
            for exercise in day["exercises"]:
                exercise["muscle_group"] = exercise["muscle_group"].value
                exercise["equipment"] = exercise["equipment"].value
                exercise["difficulty"] = exercise["difficulty"].value
                exercise["type"] = exercise["type"].value
        data["difficulty"] = data["difficulty"].value
        data["goal"] = data["goal"].value
        return data

