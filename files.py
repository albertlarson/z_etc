import os

# specify the directory you want to list files from
directory = os.getcwd()

with open('file_list.txt', 'w') as file:
    # loop through all subdirectories using os.walk()
    for root, directories, files in os.walk(directory):
        for filename in files:
            # write the full path to the file to the text file
            file.write(os.path.join(root, filename) + '\n')
