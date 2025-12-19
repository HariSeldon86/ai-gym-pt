#!/bin/sh

# Run the main application
uv run main.py

# Copy output files to the mounted output directory if it exists
if [ -d "/app/output" ]; then
  cp -f *.json /app/output/ 2>/dev/null || true
  cp -f *.toon /app/output/ 2>/dev/null || true
fi
