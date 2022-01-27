from cubic_equation import solve_cubic_equation
from linear_equation_system import LinearEquationSolver


def cubic_equation_tests():
    # test cases
    test_1 = "x^3-15x-126=0"
    sol_1 = [6]
    test_2 = "x^3-15x-4=0"
    sol_2 = [4, -3.7320508, -0.2679492]
    test_3 = "x^3+6x-20=0"
    sol_3 = [2]
    test_4 = "x^3-6x-40=0"
    sol_4 = [4]
    test_5 = "x^3-6x-4=0"
    sol_5 = [2.7320508, -2, -0.7320508]
    test_6 = "x^3-11x-14=0"
    sol_6 = [3.8284271, -2, -1.8284271]
    test_7 = "x^3-15x-14=0"
    sol_7 = [4.2749172, -3.2749172, -1]
    test_8 = "x^3 + 0x + 9 = 0"
    sol_8 = [-2.0800838]
    test_9 = "x^3-0.33333333333333333x+0.0740741=0"
    sol_9 = [-0.6666667]
    test_10 = "x^3-11x+14=0"
    sol_10 = [2, -3.8284271, 1.8284271]
    test_11 = "+5x^3+15x^2-40x+10=-10"
    sol_11 = [1, -4.8284271, 0.8284271]
    test_12 = "x^3 - x =0"
    sol_12 = [1, -1, 0]
    test_13 = "x^3 - 6x^2 + 11x =6"
    sol_13 = [3, 1, 2]
    test_14 = "2x^3 +3x^2 -11x -6 =0"
    sol_14 = [2, -3, -0.5]
    test_15 = "x^3 - 23x^2 + 142x - 120=0"
    sol_15 = [12, 1, 10]
    test_16 = "3x^3 = 6- 23x+ 16x^2"
    sol_16 = [3, 0.3333333, 2]
    test_17 = "0 = 5 + 3x - 5x^2 - 3x^3"
    sol_17 = [1, -1.6666667, -1]

    tests = [
        [test_1, sol_1],
        [test_2, sol_2],
        [test_3, sol_3],
        [test_4, sol_4],
        [test_5, sol_5],
        [test_6, sol_6],
        [test_7, sol_7],
        [test_8, sol_8],
        [test_9, sol_9],
        [test_10, sol_10],
        [test_11, sol_11],
        [test_12, sol_12],
        [test_13, sol_13],
        [test_14, sol_14],
        [test_15, sol_15],
        [test_16, sol_16],
        [test_17, sol_17],
    ]

    # test evaluation
    for test, sol in tests:
        solved = solve_cubic_equation(test)
        print(solved, end="\n\n")
        assert solved == sol

def linear_equation_system_tests():
    # test cases
    equation = [
        "3x+a-z+2y=4",
        "4z+2x-a-2y=-5",
        "+0.5y-x=3-a+z",
        "x-a+z=-6-y",
    ]
    equation_sol = {"x": 1, "y": -2, "z": -2, "a": 3}
    eq_2 = [
        "1=3x+2y-z",
        "2x-2y+4z=-2",
        "-x+0.5y-z=0",
    ]
    eq_2_sol = {"x": 1, "y": -2, "z": -2}
    eq_3 = [
        "2x + 1.5y = 7.2",
        "3x =10.2 -2y",
    ]
    eq_3_sol_rounded = {"y": 2.4, "x": 1.8}
    eq_4 = [
        "6x -y +4z =-2",
        "-x+3y-2z=9",
        "3x+2y- z= 3",
    ]
    eq_4_sol = {"x": -1, "y": 4, "z": 2}
    eq_5 = [
        "3u + 4x -5y = 39 -6z",
        "6 u + 5x -6y + 5z = 43",
        "9 u -4x + 2y + 3z = 6",
        "2   x -3y = 13-z",
    ]
    eq_5_sol = {"u": 1.0, "x": 2.0, "y": -2.0, "z": 3.0}
    eq_6 = [
        "2w - x + 3y + 2z = -5",
        "-6w - 3x - 7y = 5 + 2z",
        "4w + 4x + 5y - 5z = 13",
        "8w + 2x = -8 -2z-12y",
    ]
    eq_6_sol = {"z": -3.0, "y": -2.0, "x": -1.0, "w": 3.0}
    eqq = [
        "a + b + c = 30",
        "a + b = c + 12",
        "a + c + 2 = b + 10"
    ]
    eqq_sol = {"a": 10, "b": 11, "c": 9}

    # testing
    x = LinearEquationSolver(equation, ["x", "y", "z", "a"])
    print(x, dict(x), sep="")
    assert dict(x) == equation_sol

    y = LinearEquationSolver(eq_2, ["x", "y", "z"])
    print(y, dict(x), sep="")
    assert dict(y) == eq_2_sol

    z = LinearEquationSolver(eq_3, ["x", "y"])
    print(z)
    z = round(z)
    assert z == eq_3_sol_rounded

    for key, value in LinearEquationSolver(eq_4, ["x", "y", "z"]):
        print(f"{key} = {value}")
        assert eq_4_sol[key] == value

    a = LinearEquationSolver(eq_5, ["u", "x", "y", "z"])
    print(a, dict(a), sep="")
    assert dict(a) == eq_5_sol

    b = LinearEquationSolver(eq_6, ["w", "x", "y", "z"])
    print(b, dict(b), sep="")
    assert dict(b) == eq_6_sol
    
    qq = LinearEquationSolver(eqq, ["a", "b", "c"])
    print(qq, dict(qq), sep="")
    assert dict(qq) == eqq_sol

    x = [
        "x+y+2z=4",
        "x+2y+z=4",
        "2x+y+z=4"
    ]
    print(dict(LinearEquationSolver(x, ["x", "y", "z"])))


if __name__ == "__main__":
    cubic_equation_tests()
    linear_equation_system_tests()