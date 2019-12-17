# 保存到excel
import time


def saveToExcel(name, datas=None):
    import xlwt

    book = xlwt.Workbook()  # 新建一个excel
    sheet = book.add_sheet('case1_sheet')  # 添加一个sheet页
    row = 0  # 控制行
    for stu in datas:
        col = 0  # 控制列
        for s in stu:  # 再循环里面list的值，每一列
            sheet.write(row, col, s)
            col += 1
        row += 1
    excel_name = name + '_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.xls'
    book.save(excel_name)  # 保存到当前目录下
