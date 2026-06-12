import pandas as pd

def get_recommendations(product):

    recommendations = {

        "Laptop":[
            "Mouse",
            "Keyboard",
            "Headset"
        ],

        "Mobile":[
            "Power Bank",
            "Earbuds",
            "Case"
        ],

        "TV":[
            "Soundbar",
            "Wall Mount",
            "Remote"
        ]
    }

    return recommendations.get(
        product,
        ["No Recommendation"]
    )