#!/bin/sh

# Run the main application
uv run main.py

# Debug: List files in current directory
echo "Files in /app after running main.py:"
ls -la /app/workout_plan.json /app/workout_plan.toon 2>/dev/null || echo "No output files found"

# Copy output files to the mounted output directory if it exists
if [ -d "/app/output" ]; then
  echo "Copying files to /app/output..."
  cp -v /app/workout_plan.json /app/output/ 2>/dev/null || echo "No workout_plan.json to copy"
  cp -v /app/workout_plan.toon /app/output/ 2>/dev/null || echo "No workout_plan.toon to copy"
  echo "Files in /app/output:"
  ls -la /app/output/
else
  echo "Warning: /app/output directory does not exist"
fi
