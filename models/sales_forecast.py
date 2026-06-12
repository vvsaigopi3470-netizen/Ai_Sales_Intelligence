import numpy as np

from sklearn.linear_model import LinearRegression

def predict_sales(month):
    months = np.array(
        [
            1,2,3,4,5,6,
            7,8,9,10,11,12
        ]
    ).reshape(-1,1)

    sales = np.array(
        [
            10000,
            12000,
            14000,
            18000,
            22000,
            25000,
            28000,
            30000,
            34000,
            36000,
            40000,
            45000
        ]
    )

    model = LinearRegression()

    model.fit(
        months,
        sales
    )

    prediction = model.predict(
        [[month]]
    )

    return round(
        prediction[0],
        2
)

