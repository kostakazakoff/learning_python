import os

file_extension = input('What file extension do you search for (exe, mp3,  txt...)?: ')
system_path = input('Enter/the/path/in/system: ')


def find_file_by_extension(extension, path):
    size = 0
    output = ''
    file_list = []
    for root, dirs, files in os.walk(path):
        for searched_file in files:
            if searched_file.endswith(extension):
                file_list.append(os.path.join(root, searched_file))
    for each in file_list:
        output += str(each) + '\n'
        size += int(os.path.getsize(each))
    output += 'Total Size: ' + str(size // (1024*1024)) + ' MB'
    return output


result = find_file_by_extension(file_extension, system_path)
print(result)
