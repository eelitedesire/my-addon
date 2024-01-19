FROM homeassistant/amd64-base:3.13

# Install Python
RUN apk add --no-cache python3

# Copy your add-on files into the container
COPY . /usr/src/addon

# Set the working directory
WORKDIR /usr/src/addon

# Start your application
CMD ["python3", "app.py"]
