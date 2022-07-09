import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd

#保存数据，可用于之后的学习研究
def save_data(data, path):
    Note=open(path,mode='w')
    print("保存数据")
    Note.write(str(data))
    Note.close()

#读取xls文件数据
def read_excel(excel_name,sheet_name):
    """参数：
    输入：excel的名字
    输出：目标表的名字"""
    workbook = xlrd.open_workbook(excel_name)  #  打开文件
    sheet = workbook.sheet_by_name(sheet_name)  # 读取sheet页
    # 获取表的行列数
    rows = sheet.nrows
    cols = sheet.ncols
    all_data = []
    tempList = []
    # 读取放置在excel中的数据
    for col in range(3, 13):
        for row in range(1, rows):
            tempList.append(sheet.cell(row, col).value)
        all_data.append(tempList)
        tempList = []
    return all_data

#设置盒图的图片参数
def draw_box(all_data):
    for i in range(1):
        db = np.array(all_data)  # 把数据放置到numpy中的数组中
        print(db)
        fig = plt.figure(figsize=(40, 15))  # 设置画布大小
        ax = fig.add_subplot(111)  # 图形在画布中的布局
        allg = ["index1", "index2", "index3", "index4", "index5", "index6", "index7", "index8", "index9","index10"]  # 设置横坐标
        df = pd.DataFrame(db.T, columns=allg)  # db.T表示转置
        ax.set_title("Box-and-Whisker Plots", fontsize=24)  # 以下表示设置坐标标签以及字体大小
        ax.set_xlabel('index', fontsize=22)
        ax.set_ylabel('grade', fontsize=22)
        df.boxplot(ax=ax, fontsize=24)
        plt.savefig("盒图4.jpg")  # 保存
        plt.show()
        pd.set_option('display.max_columns', None)  # 为了将数据全部展示，显示全部列
        data = df.describe()  # 计算相关指标
        print(data)
        save_data(data, "数据.txt")  # 用于存储各组数据的指标数据


if __name__ == '__main__':
    all_data = read_excel("测试.xls", "sheet1")#读取数据
    draw_box(all_data)#绘制图表






