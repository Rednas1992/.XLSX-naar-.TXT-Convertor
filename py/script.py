import csv
import json

def download(name, extension, data_list):
    i = 1
    for data in data_list:
        with open(f"{name}-{i}.{extension}", "w") as file:
            file.write(data)
        i += 1

def jsonToCSV(json_data):
    headers = list(json_data[0].keys())
    csv_rows = [headers]

    count = 0
    max_rows = 499
    data_list = []

    for row in json_data:
        values = [row.get(header) for header in headers]
        if count == max_rows:
            count = 0
            data_list.append("\n".join([",".join(row) for row in csv_rows]))
            csv_rows = [headers]

        csv_rows.append(values)
        count += 1

    data_list.append("\n".join([",".join(row) for row in csv_rows]))
    return data_list

def convertAndDownload():
    filename = input("Enter file name: ")
    extension = input("Enter extension (csv or txt): ")
    check = input("Enter 1 for CSV or 0 for TXT: ")
    check = bool(int(check))

    with open(filename, "r") as file:
        json_data = json.load(file)

    csv_data = jsonToCSV(json_data)

    if check:
        download(filename, "csv", csv_data)
    else:
        download(filename, "txt", csv_data)

def load():
    file_path = input("Enter file path: ")
    file_name = file_path.split("\\")[-1]

    print(f"File name: {file_name}")

load()
