def read_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        print("File content:\n", content)
        file.close()

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: You do not have permission to read this file.")

    finally:
        print("File read attempt completed.")


# Function call
read_file("/home/friend/my_jupyter_project/MCA1/Aman sidar/PYTHON/PRACTICAL 1/data.txt")
