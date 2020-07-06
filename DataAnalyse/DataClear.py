import pandas as pd
from pandas import Series,DataFrame


def dataFrameFun():
    data = {"food": ["bacon", "pulled pork", "bacon", "Pastrami", "corned beef", "Bacon", "pastrami", "honey ham",
                     "nova lox"],
            "ounces": [4.0, 3.0, None, 6.0, 7.5, 8.0, -3.0, 5.0, 6.0],
            "animal": ["pig", "pig", "pig", "cow", "cow", "pig", "cow", "pig", "salmon"]}
    df = DataFrame(data)
    print_f(df)

    df = df.rename(columns={"ounces":"weight"})
    print_f(df)

    df['animal'] = df['animal'].apply(str.upper)
    print_f(df)

def print_f(value,title="source"):
    print(title,"-----------------")
    print(value)
    print(title+"-----------------")


if __name__=="__main__":
    dataFrameFun()