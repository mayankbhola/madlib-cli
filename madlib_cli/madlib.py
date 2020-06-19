import re

phrase_pattern = re.compile("\{(.*?)\}")
input_file_path = "assets/madlib_sample.txt"
output_file_path = "assets/madlib_sample_output.txt"
read_access_mode = "r"
write_access_mode = "w"

def extractor(data, pattern) :
    return pattern.findall(data)

def reader(path, mode) :
    with open(file = path, mode = mode) as f :
        data = f.read()
    return data

def writer(file, mode, data):
    with open(file = file, mode = mode) as f :
        f.write(data)

def parser(data, word_list):
    print(data)
    print(word_list)
    for word in word_list :
        data = re.sub(phrase_pattern, word, data, 1)
    return data

if __name__ == "__main__":

    data = reader(input_file_path, read_access_mode)
    phrases_list = extractor(data, phrase_pattern)
    
    word_list = []
    for phrase in phrases_list:
        word_list.append(input(f"Please provide value of phrase :: {phrase}\n"))

    result_data = parser(data, word_list)
    print(result_data)
    writer(output_file_path, write_access_mode, result_data)


