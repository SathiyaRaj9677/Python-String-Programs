# 1. Create a text file and write content

with open("example.txt", "w") as file:
    file.write("Hello, World!")

print("File created and content written.")


# 2. Write multiple lines to a file

lines = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]

with open("example.txt", "w") as file:
    file.writelines(lines)

print("Multiple lines written successfully.")



# 3. Read the entire file

with open("example.txt", "r") as file:
    content = file.read()

print(content)



# 4. Read a file line by line

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())


# 5. Append content to an existing file

with open("example.txt", "a") as file:
    file.write("\nThis is additional content.")

print("Content appended successfully.")




# 6. Check whether a file exists

import os

if os.path.isfile("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")



# 7. Count lines, words, and characters in a file

with open("example.txt", "r") as file:
    content = file.read()

print("Lines:", len(content.splitlines()))
print("Words:", len(content.split()))
print("Characters:", len(content))



# 8. Search for a word in a file

search_word = "Python"

with open("example.txt", "r") as file:
    content = file.read()

if search_word.lower() in content.lower():
    print("Word found.")
else:
    print("Word not found.")



# 9. Rename a file

import os

if os.path.isfile("example.txt"):
    os.rename("example.txt", "renamed.txt")
    print("File renamed successfully.")
else:
    print("File not found.")



# 10. Copy a file

import shutil

shutil.copy("renamed.txt", "copy.txt")

print("File copied successfully.")



# 11. Delete a file

import os

file_path = "copy.txt"

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File not found.")



# ========================================================================

# 12. Create a directory

import os
os.makedirs("Python_Practice", exist_ok=True)
print("Directory created successfully.")



# 13. List files and folders in a directory

import os
directory = "."
for item in os.listdir(directory):
    print(item)


# 14. Delete an empty directory

import os
directory = "Python_Practice"
if os.path.isdir(directory) and not os.listdir(directory):
    os.rmdir(directory)
    print("Empty directory deleted.")
else:
    print("Directory does not exist or is not empty.")



# 15. Get file size

import os

file_path = "example.txt"
if os.path.isfile(file_path):
    size = os.path.getsize(file_path)
    print("File size:", size, "bytes")
else:
    print("File not found.")

# ================================================================================

# 16. Write data to a CSV file

import csv

data = [
    ["Name", "Age", "Country"],
    ["John", 25, "India"],
    ["Jane", 30, "Canada"],
    ["Bob", 40, "Australia"]
]
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully.")


# 17. Read data from a CSV file

import csv
with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



# 18. Append a row to a CSV file

import csv

new_student = ["Sathya", 33, "India"]
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_student)
print("New row added successfully.")



# 19. Read CSV data using a dictionary

import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"], row["Country"])



# 20. Delete a row from a CSV file by name

import csv

filename = "students.csv"
name_to_delete = "Jane"

with open(filename, "r", newline="") as file:
    reader = csv.reader(file)
    rows = list(reader)

if rows:
    header = rows[0]
    filtered_rows = [
        header
    ] + [
        row for row in rows[1:]
        if row and row[0] != name_to_delete
    ]

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(filtered_rows)
    print("CSV data updated successfully.")




# 21. Search for a record in a CSV file

import csv

search_name = "John"

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    found = False

    for row in reader:
        if row["Name"].lower() == search_name.lower():
            print(row)
            found = True

    if not found:
        print("Record not found.")


#======================================================================

# 22. Write binary data to a file

with open("binary_file.bin", "wb") as file:
    file.write(b"Hello, World!")

print("Binary data written successfully.")



# 23. Read binary data from a file

with open("binary_file.bin", "rb") as file:
    data = file.read()

print(data)
print(data.decode("utf-8"))



# 24. Copy a binary file

import shutil
shutil.copyfile("binary_file.bin", "binary_copy.bin")
print("Binary file copied successfully.")



# 25. Clear the contents of a file

filename = "binary_file.bin"
with open(filename, "wb") as file:
    pass

print("File contents cleared.")



#==========================================================


# 26. Create a ZIP file and add files

import zipfile

with zipfile.ZipFile("example.zip", "w") as archive:
    archive.write("example.txt")
    archive.write("students.csv")

print("ZIP file created successfully.")



# 27. List files inside a ZIP archive

import zipfile

with zipfile.ZipFile("example.zip", "r") as archive:
    for filename in archive.namelist():
        print(filename)



# 28. Extract all files from a ZIP archive

import zipfile

with zipfile.ZipFile("example.zip", "r") as archive:
    archive.extractall("extracted_files")

print("Files extracted successfully.")



# 29. Add text content to a ZIP archive

import zipfile

with zipfile.ZipFile("example.zip", "a") as archive:
    archive.writestr(
        "notes.txt",
        "These are Python practice notes."
    )

print("Text file added to ZIP archive.")



# 30. Remove a file from a ZIP archive
# ZIP files do not support direct deletion.
# Create a replacement archive without the selected file.

import zipfile
import os

source_zip = "example.zip"
replacement_zip = "replacement.zip"
file_to_remove = "example.txt"

with zipfile.ZipFile(source_zip, "r") as source:
    with zipfile.ZipFile(replacement_zip, "w") as replacement:
        for item in source.infolist():
            if item.filename != file_to_remove:
                replacement.writestr(item, source.read(item.filename))

os.replace(replacement_zip, source_zip)

print("ZIP archive updated successfully.")



# ===========================================================================

# 31. Handle a file that does not exist

try:
    with open("missing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist.")



# 32. Read and write using r+ mode

with open("example.txt", "w") as file:
    file.write("Python File Handling")

with open("example.txt", "r+") as file:
    content = file.read()
    print("Original content:", content)

    file.write("\nNew content")

with open("example.txt", "r") as file:
    print(file.read())



# 33. Read only the first five characters

with open("example.txt", "r") as file:
    print(file.read(5))




# 34. Read a file using seek() and tell()

with open("example.txt", "r") as file:
    print("Initial position:", file.tell())

    print("First five characters:", file.read(5))
    print("Current position:", file.tell())

    file.seek(0)
    print("After resetting:", file.read(5))


#================================================================================

# 35. Write test results to a text file

test_results = [
    "test_login: PASS",
    "test_search: PASS",
    "test_payment: FAIL"
]

with open("test_results.txt", "w") as file:
    for result in test_results:
        file.write(result + "\n")

print("Test results saved.")



# 36. Count passed and failed tests from a report

passed = 0
failed = 0

with open("test_results.txt", "r") as file:
    for line in file:
        if "PASS" in line:
            passed += 1
        elif "FAIL" in line:
            failed += 1

print("Passed tests:", passed)
print("Failed tests:", failed)



# 37. Save API response data to JSON

import json

response_data = {
    "status_code": 200,
    "message": "Success",
    "user": {
        "id": 101,
        "name": "Sathya"
    }
}

with open("api_response.json", "w") as file:
    json.dump(response_data, file, indent=4)

print("API response saved.")



# 38. Read API response data from JSON

import json

with open("api_response.json", "r") as file:
    response_data = json.load(file)

print("Status code:", response_data["status_code"])
print("Message:", response_data["message"])
print("User name:", response_data["user"]["name"])



# 39. Validate an API response saved in JSON

import json

with open("api_response.json", "r") as file:
    response = json.load(file)

assert response["status_code"] == 200
assert response["message"] == "Success"
assert response["user"]["id"] == 101

print("API response validation passed.")



# 40. Save application logs with timestamps

from datetime import datetime

message = "Login test executed successfully"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("application.log", "a") as file:
    file.write(f"{timestamp} - {message}\n")

print("Log entry saved.")
