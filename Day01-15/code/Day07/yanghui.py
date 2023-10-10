def main():
    num = int(input('Number of rows: '))
    yh = []  # 创建一个空列表用于存储杨辉三角
    for row in range(num):
        # 初始化当前行的子列表，每一行都应该是一个独立的子列表
        current_row = [1]  # 每一行的第一个元素都是1
        if row > 1:
            # 计算中间的元素
            for col in range(1, row):
                tmp = yh[row - 1][col - 1] + yh[row - 1][col]
                current_row.append(tmp)
        if row > 0:
            current_row.append(1)  # 每一行的最后一个元素都是1
        yh.append(current_row)  # 将当前行添加到杨辉三角列表
    # 打印杨辉三角
    for row in yh:
        for num in row:
            print(num, end='\t')
        print()

if __name__ == '__main__':
    main()
