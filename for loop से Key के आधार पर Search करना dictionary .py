student = {
    "name": "Gourav",
    "age": 25,
    "course": "MCA"
}

search_key = "course"

for key in student:
    if key == search_key:
        print(key, student[key])
