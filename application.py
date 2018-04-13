from flask import Flask
from flask import render_template
from flask import jsonify

import requests
import os
import json
import re

app = Flask(__name__)

# Get Information on Environment - And Task Metadata if Environment is ECS
def get_task_metadata(platform):
    try:
      if platform == "ECS":
          response = requests.get('http://169.254.170.2/v2/metadata')
          if response.status_code == 200:
              data = re.sub('^.*[0-9]{12}.*$', 'REDACTED', json.dumps(response.json(), sort_keys = True, indent = 4, separators = (',', ': ')))
              return data
          else:
              return "The application is running in ECS but it could not connect to the metadata endpoint."
    except:
      return "APP_ENV is not correctly defined as an environment variable. Ensure APP_ENV is set to LOCAL, DOCKER or ECS."

def get_platform_message(platform):
    try:
      if platform == "ECS":
          return "The application is running on ECS."
      elif platform == "LOCAL":
          return "The application is running locally."
      elif platform == "DOCKER":
          return "The applicatipn is running locally in a container."
    except:
      return "APP_ENV is not correctly defined as an environment variable. Ensure APP_ENV is set to LOCAL, DOCKER or ECS."

def get_service_endpoints():
    try:
        return ""
    except:
        return "Unable to find any service endpoints."

@app.route('/')
def hello():
    message = "Welcome to the Containers Immersion Day!"
    platform = get_platform_message(os.environ['APP_ENV'])
    metadata = get_task_metadata(os.environ['APP_ENV'])
    endpoints = get_service_endpoints()
    return render_template('application.html', message=message, platform=platform, metadata=metadata, endpoints=endpoints)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
