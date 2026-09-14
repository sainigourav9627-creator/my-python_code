try:
    with open("student.txt", "r") as file:
        data = file.read()

    print("File Content:")
    print(data)

except FileNotFoundError:
    print("student.txt file nahi mili.")

except PermissionError:
    print("File access karne ki permission nahi hai.")

finally:
    print("File operation completed.")
