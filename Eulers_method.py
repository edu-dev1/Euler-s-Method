import matplotlib.pyplot as plt

functions = {
    "f1": {
        "f" : lambda x, y : y - (x ** 2) + 1,
        "f_str" : "y - x² + 1",  
        "h" : 0.2,
        "y0" : 0.5,
        "x_coor" : [],
        "y_coor" : [],
        "expressions" : []},
    "f2": {
        "f" : lambda x, y : (3 * y) - (4 * x),
        "f_str" : "3y - 4x",
        "h" : 0.25,
        "y0" : 1,
        "x_coor" : [],
        "y_coor" : [],
        "expressions" : []},
    "f3": {
        "f" : lambda x, y : (y ** 2) - x,
        "f_str" : "y² - x",
        "h" : 0.1,
        "y0" : 1,
        "x_coor" : [],
        "y_coor" : [],
        "expressions" : []},
    "f4": {
        "f" : lambda v : -0.98 - (0.1 * v),
        "f_str" : "-0.98 - 0.1v",
        "h" : 0.5,
        "y0" : 0,
        "x_coor" : [],
        "y_coor" : [],
        "expressions" : []}
}

for func in functions.keys():
        
    x = 0
    f = functions[func]["f"]
    h = functions[func]["h"]
    y = functions[func]["y0"]
    f_str = functions[func]["f_str"]
    expressions = functions[func]["expressions"]
    expression = f_str

    print(func, "y' =", functions[func]["f_str"], f", h = {h}")
    print(f"\ty0 -> y({x}) = {y}")
    
    for n in range(1, int(1.0 / h) + 1):
        x_axis = functions[func]["x_coor"]
        y_axis = functions[func]["y_coor"]

        x_axis.append(x)
        y_axis.append(y)

        expressions.append(f_str)
        expression = expressions[n - 1]

        if func == "f4":
            next_y = y + h * (f(y)) # Euler
            expression = expression.replace("v", "(" + str(round(y, 2)) + ")")
        else:
            next_y = y + h * (f(x, y)) # Euler
            expression = expression.replace("x", str(round(x, 2)))
            expression = expression.replace("y", str(round(y, 2)))

        next_x = x + h # Euler

        print(f"\ty{n} -> y({next_x:.1f}) = [{y:.4f} + {h}({expression})] = \033[1;33m{next_y:.4f}\033[0m")
                                                                            # 1 = Negrita, ;33 = amarillo, 0 = reset

        x = next_x
        y = next_y

        x_axis.append(x)
        y_axis.append(y)
    
    plt.plot(x_axis, y_axis, "o-", color = "red")
    plt.title(func, loc="left")
    plt.title(f_str, loc="center")
    plt.title(f"h = {h}", loc="right")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.savefig(func)
    plt.show()