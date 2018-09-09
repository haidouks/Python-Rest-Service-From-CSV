import sys
import json
from flask_restful import Resource
from flask import jsonify,abort,request
import csv_data

class CSVToRest(Resource):
    csvFile = ""
    def get(self):
        csvDatas = csv_data.get_csv_data(self.csvFile,";")
        result = []
        queries = [] 
        if(request.query_string):
            queryStrings = request.query_string.split("&")
            for queryString in queryStrings:
                query = {}
                query["{}".format(queryString.split("=")[0])] = queryString.split("=")[1]
                queries.append(query)
        else:
            return csvDatas
        print("Queries: {}".format(queries))
        for csvData in csvDatas:
            print("csvData: {}".format(csvData))
            add = True
            for query in queries:
                print("QueryKey: {}".format(query))
                if(csvData[query.keys()[0]] != query.values()[0]):
                    add = False
            if add:
                result.append(csvData)
        return result