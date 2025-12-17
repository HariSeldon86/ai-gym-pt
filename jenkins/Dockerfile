FROM python:3.12-slim

WORKDIR /app

# Install UV
RUN pip install --no-cache-dir uv

# Copy project files
COPY pyproject.toml uv.lock* ./
COPY . .

# Install dependencies using lock file
RUN uv sync --locked

# Run the application
ENTRYPOINT ["uv", "run", "main.py"]