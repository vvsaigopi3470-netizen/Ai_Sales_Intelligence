import pandas as pd

from sklearn.cluster import KMeans

def segment_customers():

    data = {

        "purchase":[
            1000,
            2000,
            5000,
            7000,
            15000,
            25000,
            30000
        ]
    }

    df = pd.DataFrame(data)

    model = KMeans(
        n_clusters=3,
        random_state=42
    )

    df['segment'] = model.fit_predict(
        df[['purchase']]
    )

    return df.to_dict(
        orient='records'
    )