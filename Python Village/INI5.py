#INI5
file_path="put your file path here"
with open(file_path, encoding='utf8') as f:
    for count, line in enumerate(f, start=1):
        if count % 2 == 0:
            print(line)