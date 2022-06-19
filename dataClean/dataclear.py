import csv
import os
import json
#引用库

config = json.load(open("config.json", encoding='utf-8'))
read_report_path = config["read_report_path"]
#报表路径
write_report_path = config["write_report_path"]
#写入报表的路径
read_report_names = os.listdir(read_report_path)
#读取的文件名列表
read_tradata_path = config["read_tradata_path"]
#交易数据路径
write_tradata_path = config["write_tradata_path"]
#写入交易数据的路径
read_tradata_names = os.listdir(read_tradata_path)
#读取的文件名列表


def check_report_row(row_list):
    for i in row_list[1:]:
        try:
            i = float(i)
            if not i:
                return False
        except:
            return False
    return True
# 检查行中是否有非法字符或者零值。为报表设计。


def check_tradata_row(row_list):
    for i in row_list[3:]:
        try:
            i = float(i)
            if not i:
                return False
        except:
            return False
    return True
# 检查行中是否有非法字符或者零值。为交易数据设计。


def clear_report(is_all=True, file=""):  #is_all是所有读取，file是单个读取时文件的名字
    # 报表的清洗以及转置
    temp_list = []  #存放转置列表
    if is_all:
        for read_file_name in read_report_names:  # 对文件夹下的所有文件进行操作
            read_file_path = read_report_path + '\\' + read_file_name  # 单个文件路径
            with open(read_file_path, 'rt') as rf:   #打开要读取的csv文件，rt代表以只读text格式打开，with open会在运行完后自动关闭文件
                read_file = csv.reader(rf)   #以reader方式读取行信息的集合
                for row in read_file:
                    row = row[:-1]  #逐行读取，并去掉尾部的空格符
                    if not row:
                        break  #最后两行会出现['\t\t']和['']，去掉尾部后为空，要去掉
                    temp_list.append(row)  #将该行添加
                temp_list = list(map(list, zip(*temp_list)))  #转置列表

                write_file_name = write_report_path + '\\' + read_file_name[:-4] + 'checked.csv'  #写入结果的文件名
                with open(write_file_name, 'wt') as wf:  #创建要写入的csv文件
                    write_file = csv.writer(wf, lineterminator='\n')   #赋予文件变量，lineterminator代表分隔符，不如此设定则会出现空行
                    t = 0  #控制第一行中文要读取
                    for row in temp_list:   #按行读取
                        if t == 0:
                            for i in range(24):
                                row[i] = config[row[i]]
                            write_file.writerow(row)  # 写入文件
                            t = 1  # 后面的就不用改了
                        if check_report_row(row):   #check
                            write_file.writerow(row)   #写入文件

    else:
        read_file_path = read_report_path + '\\' + file # 单个文件路径
        with open(read_file_path, 'rt') as rf:  # 打开要读取的csv文件，rt代表以只读text格式打开，with open会在运行完后自动关闭文件
            read_file = csv.reader(rf)  # 以reader方式读取行信息的集合
            for row in read_file:
                row = row[:-1]  # 逐行读取，并去掉尾部的空格符
                if not row:
                    break  # 最后两行会出现['\t\t']和['']，去掉尾部后为空，要去掉
                temp_list.append(row)  # 将该行添加
            temp_list = list(map(list, zip(*temp_list)))  # 转置列表
            write_file_name = write_report_path + '\\' + file[:-4] + 'checked.csv'  # 写入结果的文件名
            with open(write_file_name, 'wt') as wf:  # 创建要写入的csv文件
                write_file = csv.writer(wf, lineterminator='\n')  # 赋予文件变量，lineterminator代表分隔符，不如此设定则会出现空行
                t = 0  # 控制第一行中文要读取
                for row in temp_list:  # 按行读取
                    if t == 0:
                        for i in range(24):
                            row[i] = config[row[i]]
                        write_file.writerow(row)  # 写入文件
                        t = 1  # 后面的就不用改了
                    if check_report_row(row):  # check
                        write_file.writerow(row)  # 写入文件



def clear_tradata(is_all=True, file=""):  #is_all是所有读取，file是单个读取时文件的名字
    #交易数据的清洗
    if is_all:
        for read_file_name1 in read_tradata_names:  # 对文件夹下的所有文件进行操作
            read_file_path1 = read_tradata_path + '\\' + read_file_name1  # 单个文件路径
            with open(read_file_path1, 'rt') as rf:   #打开要读取的csv文件，rt代表以只读text格式打开，with open会在运行完后自动关闭文件
                read_file1 = csv.reader(rf)   #以reader方式读取行信息的集合
                write_file_name1 = write_tradata_path + '\\' + read_file_name1[:-4] + 'checked.csv'  #写入结果的文件名
                with open(write_file_name1, 'wt') as wf:  #创建要写入的csv文件
                    write_file1 = csv.writer(wf, lineterminator='\n')   #赋予文件变量，lineterminator代表分隔符，不如此设定则会出现空行
                    adc = 0  #控制第一行中文要读取
                    for row1 in read_file1:   #按行读取
                        if adc == 0:
                            for i in range(15):
                                row1[i] = config[row1[i]]
                            write_file1.writerow(row1)
                        if adc == 1:
                            name = row1[2]  #去标点
                        if check_tradata_row(row1):   #check
                            row1[1] = str(row1[1][1:])
                            row1[2] = name
                            write_file1.writerow(row1)   #写入文件
                        adc += 1  #后面的不符合就不用读了

    else:
        read_file_path1 = read_tradata_path + '\\' + file  # 单个文件路径
        with open(read_file_path1, 'rt') as rf:  # 打开要读取的csv文件，rt代表以只读text格式打开，with open会在运行完后自动关闭文件
            read_file1 = csv.reader(rf)  # 以reader方式读取行信息的集合
            write_file_name1 = write_tradata_path + '\\' + file[:-4] + 'checked.csv'  # 写入结果的文件名
            with open(write_file_name1, 'wt') as wf:  # 创建要写入的csv文件
                write_file1 = csv.writer(wf, lineterminator='\n')  # 赋予文件变量，lineterminator代表分隔符，不如此设定则会出现空行
                adc = 0  # 控制第一行中文要读取
                for row1 in read_file1:  # 按行读取
                    if adc == 0:
                        for i in range(15):
                            row1[i] = config[row1[i]]
                        write_file1.writerow(row1)
                    if adc == 1:
                        name = row1[2]  # 去标点
                    if check_tradata_row(row1):  # check
                        row1[1] = str(row1[1][1:])
                        row1[2] = name
                        write_file1.writerow(row1)  # 写入文件
                    adc += 1  # 后面的不符合就不用读了


if __name__ == '__main__':
    clear_report()
    clear_tradata()
    