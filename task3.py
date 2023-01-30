import os

def create_combined_list(directory):
    files = os.listdir(directory)
    combined_list = []

    for file in files:
        with open(directory + "/" + file) as cur_file:
            combined_list.append([file, 0, []])
            for line in cur_file:
                combined_list[-1][2].append(line.strip())
                combined_list[-1][1] += 1
                # print(line)

    return sorted(combined_list, key=lambda x: x[2], reverse=True)


def create_file_from_directory(directory, filename):
    with open(filename + '.txt', 'w+') as newfile:
        for file in create_combined_list(directory):
            newfile.write(f'File name: {file[0]}\n')
            newfile.write(f'Length: {file[1]} string(s)\n')
            # print(file)
            for string in file[2]:
                newfile.write(string + '\n')
                # print(string)
            newfile.write('-------------------\n')


print(create_file_from_directory('sorted', 'newfiletxt'))