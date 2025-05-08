def read_and_modify():
    try:
        input_file = input("Please enter the name of the file: ")
        with open(input_file, 'r') as f:
            content = f.read()
        modified_content = content.upper()
        modified_file = f"modified_{input_file}"

        with open(modified_file, 'w') as f:
            f.write(modified_content)
        print(f"The file has been updated and saved to {modified_file}")

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("There was a problem reading the file")
    except Exception as e:
        print(f"An unexpected error occured{e}")

read_and_modify()