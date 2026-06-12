import plotly.express as px
import pandas as pd

def revenue_chart():

    df = pd.DataFrame({

        "Month":[
            "Jan",
            "Feb",
            "Mar",
            "Apr"
        ],

        "Revenue":[
            100000,
            150000,
            180000,
            250000
        ]
    })

    fig = px.bar(
        df,
        x='Month',
        y='Revenue',
        title='Revenue Analysis'
    )

    return fig.to_html(
        full_html=False
    )