from flask import Flask
from flask import render_template
from flask import jsonify

import requests
import os
import json

app = Flask(__name__)

# Get Information on Environment - And Task Metadata if Environment is ECS
def get_task_metadata(environment):
    try:
      if environment == "ECS":
          response = requests.get('http://169.254.170.2/v2/metadata')
          if response.status_code == 200:
              return response.content
          else:
              return "The application is running in ECS but it could not connect to the metadata endpoint."
      elif environment == "DOCKER":
        return "The application is running locally in a Docker container."
      elif environment == "LOCAL":
        return "The application is running locally."
    except:
      return "APP_ENV is not correctly defined as an environment variable. Ensure APP_ENV is set to LOCAL, DOCKER or ECS."

@app.route('/')
def hello():
    message = "Welcome to the Containers Immersion Day!"
    metadata = get_task_metadata(os.environ['APP_ENV'])
    return render_template('application.html', message=message, metadata=metadata)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
