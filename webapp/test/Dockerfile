FROM continuumio/miniconda3

RUN conda install -y nltk bokeh numpy pandas

# Set the working directory to /app
WORKDIR /app

COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD bokeh serve --allow-websocket-origin=18.222.239.0 map.py
