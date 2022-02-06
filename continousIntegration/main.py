##### IMPORTS #####

from flask import Flask, request, json
import os
import sys

##### SETTINGS #####

STATUS_DEBUG = True
HOST = "127.0.0.1"
PORT = 8080

PATH_REPO = '' # Folder within CWD to run the code.

##### PROGRAM #####

app = Flask(__name__) # Variable for flask server application, to be called upon.

# Create an endpoint which receives requests from the GitHub API.
@app.route('/', methods=['POST']) # Triggered by URL localhost:5000/
def handler_Push():

    data = request.json # Request the data from the event.

    print("Received PUSH event from webhook!") # Debug print.

    # TODO: Extract Repository.
    # TODO: Save relevant parts of repo into variables to send to the other scripts.

    # Here you do all the continuous integration tasks
    # For example:
    # 1st clone your repository
    # 2nd compile the code

    # Step 1: Clone the repository.
    branch = data["repository"]["clone_url"] # Fetches the clone URL from the payload.

    os.chdir(os.getcwd + PATH_REPO) # Changes current directory to where the cloned repository is to be located.
    os.system("git clone " + branch) # Runs command to clone the repository.

    # TODO: Run module that compiles.
    # TODO: Run module that tests.

    #Flask.Response(status=200)
    return "OK" # Defaults to 200 response code.


# Start the Flask web server.
if __name__ == '__main__':
    app.run(debug=STATUS_DEBUG, host=HOST, port=PORT)