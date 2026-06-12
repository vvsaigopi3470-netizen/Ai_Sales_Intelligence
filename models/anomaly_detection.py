import pandas as pd

from sklearn.ensemble import (
    IsolationForest
)

def detect_anomalies():

    df = pd.DataFrame({

        'sales':[
            100,
            120,
            115,
            130,
            110,
            600,
            125
        ]
    })

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    df['anomaly'] = model.fit_predict(
        df[['sales']]
    )

    anomalies = df[
        df['anomaly'] == -1
    ]

    return anomalies.to_dict(
        orient='records'
    )