from flask import Flask
import sys
import os

path, filename = os.path.split(__file__)
modulePath = "{}/modules".format(path)

sys.path.append(r'{}'.format(modulePath))
import json
from flask_restful import Api
from csv_to_rest import CSVToRest

app = Flask(__name__)
api = Api(app)

CSVToRest.csvFile = "{}/data/sample.csv".format(path)
api.add_resource(CSVToRest, "/CSVToRest")
app.run(debug=True)



