# 计算函数
def calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2


# 检查输入的运算符规范性函数
def check_operator(operator):
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        return True
    else:
        return False


# 录入运算符号的处理函数
def input_operator():
    a = input('请输入运算符号（+ - * /）：')
    while True:
        if check_operator(a):
            return a
        else:
            a = input('运算符不正确！请重新输入（+ - * /）：')


# 输入的第二个数的处理函数
def input_num2(operator):
    num2 = float(input('请输入第二个数：'))
    while True:
        if operator == '/' and num2 == 0:
            num2 = float(input('除数不能为0，请重新输入第二个数：'))
        else:
            return num2


Exit_Flag = 'N'
while Exit_Flag == 'N':
    # 输入第一个数
    Input_num1 = float(input('请输入第一个数：'))
    # 输入运算符
    Input_operator = input_operator()
    # 输入第二个数
    Input_num2 = input_num2(Input_operator)
    # 进行运算并打印出运算结果
    Result = calc(Input_num1, Input_num2, Input_operator)
    print('运算结果为：', Result)
    Exit_Flag = input('是否退出计算器模式：Y（退出）/ N（继续）：')

