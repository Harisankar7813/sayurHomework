import os
def binary_file(directory_name,file_name,content):
    if not os.path.exists(directory_name):
        os.mkdirs(directory_name)
    file_path=os.path.join(directory_name,file_name)
    with open('file_path','wb') as file:
        file.write(content)
    print(f"The content has been written in {file_name} {directory_name}")

directory_name="F:"
file_name="newexample.bin"
content=b"this is a bin content"
binary_file(directory_name,file_name,content)