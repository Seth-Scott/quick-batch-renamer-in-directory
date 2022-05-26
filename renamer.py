import os

directory = input("What's the directory name?")
path = f"/{directory}"
files = os.listdir(path)

counter = 1
for file in range(len(files)):
    os.rename(path+files[file], f"{directory}_{counter}")
    print(file)

