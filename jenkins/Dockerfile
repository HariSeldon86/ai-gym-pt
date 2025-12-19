FROM python:3.12-slim

WORKDIR /app

# Install UV
RUN pip install --no-cache-dir uv

# Copy project files
COPY . .

# Install dependencies and make run script executable
RUN uv sync --locked && chmod +x jenkins/run.sh

# Run the application
ENTRYPOINT ["/app/jenkins/run.sh"]