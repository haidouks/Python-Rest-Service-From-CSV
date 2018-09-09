import csv

def get_csv_data(csvPath, csvDelimiter):
    csv_rows = []
    csvFile = open(csvPath,'r')
    reader = csv.DictReader(csvFile,delimiter=csvDelimiter)
    fields = reader.fieldnames
    for readerRow in reader:
        row = {}
        for field in fields:
            row[field] = readerRow[field]
        csv_rows.append(row)
    return csv_rows
