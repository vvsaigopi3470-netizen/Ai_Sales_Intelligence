from models.sales_forecast import (
    predict_sales
)

def test_forecast():

    result = predict_sales(5)

    assert result > 0