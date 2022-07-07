# -*- coding: utf-8 -*-

import os
def read_files():
    """该函数用于读取对应文件夹下各文件的名字"""
    path = input("目标文件夹：") + '/'
    files = os.listdir(path)
    file_names=[]
    for file in files:
        if file.split('.')[-1] =='txt':
            file_names.append(file)
    return  path,file_names

def mixed_file( path,files):
    """该函数用于合并刚才读取的各文件
    输入：文件路径，read_files()返回的文件名
    输出：一个合并后的文件"""
    content = ''
    for file_name in files:
        with open( path+file_name , 'r' ,encoding='utf-8') as file:
            content = content + file.read()
            file.close()
       
    with open(path + '合并后的文件.txt', 'a',encoding='utf-8') as file:
        file.write(content)
        content = ''
        file.close()




if __name__ == '__main__':
    path,files = read_files()
    mixed_file( path,files)
