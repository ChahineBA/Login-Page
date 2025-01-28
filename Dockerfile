# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app runs on
EXPOSE 5000

# Set environment variables (optional)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV MONGO_URI=${MONGO_URI}
ENV MONGO_DB=${MONGO_DB}
ENV MONGO_COLLECTION=${MONGO_COLLECTION}

# Run the Flask app
CMD ["flask", "run"]
