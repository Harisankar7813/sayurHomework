import os
def create_dict(directory_name,file_name,content):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    file_path=os.path.join(directory_name,file_name)

    with open(file_path,'w') as file:
        file.write(content)
    print(f"file '{file_name} created inside directory {directory_name}.")

directory_name="F:\seyur home work\Preperation\Filehandling"
file_name="new_example.txt"
content="this is a content"
result=create_dict(directory_name,file_name,content)


