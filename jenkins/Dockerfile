FROM python:3.12-slim

WORKDIR /app

# Install UV
RUN pip install --no-cache-dir uv

# Copy project files
COPY pyproject.toml uv.lock* ./
COPY . .

# Install dependencies using lock file
RUN uv sync --locked

# Create output directory and copy run script
RUN mkdir -p /app/output
COPY jenkins/run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Run the application
ENTRYPOINT ["/app/run.sh"]