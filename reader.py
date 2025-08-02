def read_and_modify_file():
    try:
        # Ask the user for the filename
        input_filename = input("Enter the name of the file to read (Hello world): ")

        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read("text")

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper(" fine us about ")

        # Write modified content to a new file
        with open("modified_output.txt", 'w') as outfile:
            outfile.write(modified_content)

        print("File read and modified successfully.")
        print("Modified content written to 'modified_output.txt'.")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: Could not read the file.")

# Run the function
read_and_modify_file()
