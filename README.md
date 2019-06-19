# vggm-webapp
This repository containerize Bokeh server and Flask server using docker compose
Usage:

    1. Pull this repository
    2. Install docker and docker compose
    3. $ cd vggm-webapp
    4. $ docker-compose up
The application will be up at http://localhost:80.

Note: If you want to deploy this application on a remote machine, change the "localhost" in app.py and bokehapp.Dockerfile to the ip address of the remote machine.
