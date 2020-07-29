var_a = input( "Введите первое значение: ")
var_b = input( "Введите второе значение: ")
def func(var_a, var_b):
    try:
        var_a = float(var_a)
        var_b = float(var_b)
        if var_a > var_b:
            print(">")
        elif var_a < var_b:
            print("<")
        elif var_a == var_b:
            print("=")
    except:
        print("string")
func(var_a, var_b)