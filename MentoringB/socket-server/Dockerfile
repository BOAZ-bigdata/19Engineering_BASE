# base image

# Use an official Python runtime as a parent image
FROM python:3.8.6 

# Set the working directory to /app
WORKDIR /app

# update fundamentals
RUN apt-get update && apt-get install -y

# Copy the current directory contents into the container at /app
COPY . app/ 

# Install any needed packages specified in requirements.txt
RUN pip3 install -r app/requirements.txt

# Make port 9080 available to the world outside this container
EXPOSE 9080

# Define environment variable
# ENV NAME World

RUN cd app/

# Run app.py when the container launches
CMD [ "python3", "app/server.py"]
