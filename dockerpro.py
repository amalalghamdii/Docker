import os
import socket
import sys 
from collections import Counter

#stdoutOrigin=sys.stdout 
#sys.stdout = open("/home/output/result.txt", "w")


ip_address = socket.gethostbyname(socket.gethostname())
print("IP Address:", ip_address)

directory = '/home/data'


def print_text_files(directory):
    print("List the text files in the directory:")
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            print(filename)



def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

def count_total_words(directory):
    total_words = 0
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            file_word_count = count_words_in_file(file_path)
            total_words += file_word_count
            print(f"{filename}, Word count: {file_word_count}")
    print("Total word count in all text files:", total_words)


def count_word_occurance(file):
    d = dict() 
    for line in file: 
        line = line.strip() 
        line = line.lower() 
        words = line.split(" ") 
        for word in words: 
            if word in d: 
                d[word] = d[word] + 1
            else: 
                d[word] = 1
    return d

dir = os.listdir(directory)
if len(dir) != 0:
    print_text_files(directory)
    count_total_words(directory)
    file2 = "IF.txt"
    file_path = os.path.join(directory, file2)
    if os.path.exists(file_path):
        o_file = open(file_path ,"r")
        file_count = count_word_occurance(o_file)
        file_sort = dict(sorted(file_count.items(), key=lambda item: item[1], reverse=True))
        print("the most occurrence word in the IF.txt")
        for i, (key, value) in enumerate(file_sort.items()):
            print(key, ":", value)
            if i == 2:  
                break


sys.stdout.close()

directory2 = '/home/output'
dir_output = os.listdir(directory2)
if len(dir_output) != 0:
    for line in dir_output:
        output_file = open(dir_output ,"r")
        print(line, end='')










