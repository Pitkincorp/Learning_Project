def longest_word_in_file(file_name):
    file = open(file_name, encoding='utf-8')
    for i in file.readlines():
        print(i)


longest_word_in_file(r'C:\Users\YaYuBeletskiy\AppData\Local\Programs\Python\Python39\Myscripts\example.txt')
