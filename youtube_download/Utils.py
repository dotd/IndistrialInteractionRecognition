def load_string(full_path_and_file):
    text_file = open(full_path_and_file, "r")
    res = text_file.read()
    text_file.close()
    return res
