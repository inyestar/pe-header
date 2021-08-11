def read_byte(file_name):
    with open(file_name, 'rb') as f:
        lines = f.readlines()
        for line in lines:
            print(line)


