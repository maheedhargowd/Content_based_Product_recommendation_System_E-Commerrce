# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 7860 (default for Hugging Face)
EXPOSE 7860

# Run the API
CMD ["streamlit", "run", "app.py", "--server.port", "7860", "--server.address", "0.0.0.0"]





