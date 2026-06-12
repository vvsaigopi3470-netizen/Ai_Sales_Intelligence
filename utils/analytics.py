import pandas as pd
import plotly.express as px

from database.mysql_db import mysql

def generate_sales_chart():

    query = """
    SELECT
    sale_date,
    SUM(revenue) revenue

    FROM sales

    GROUP BY sale_date
    """

    df = pd.read_sql(
        query,
        mysql.connection
    )

    fig = px.line(
        df,
        x="sale_date",
        y="revenue",
        title="Revenue Trend"
    )

    return fig.to_html(
        full_html=False
    )