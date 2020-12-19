if __name__ == '__main__':
    str = "56220,73900,79564,25631,68321,49600,67200," \
          "96000,47100,87500,68500,101700,39500,3564,23600"
    list = str.split(",")
    for i in range(0, len(list)):
        list[i] = int(list[i])
    print("最大值：", max(list))
    print("最小值：", min(list))
    print("总 和：", sum(list))
