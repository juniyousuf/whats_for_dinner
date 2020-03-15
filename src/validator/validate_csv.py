import pandas as pd
from datetime import date


measuring_type = ['slice', 'grams', 'ml, slices']

def validate_csv_data(df):

    today = date.today()
    # dd/mm/YY
    date_today = today.strftime("%d/%m/%Y")

    df["Use By Date"]= pd.to_datetime(df["Use By Date"]) 

    is_measure_unit_correct = df["Unit Of Measure"].isin(measuring_type).all()

    is_quantity_correct = (df["Quantity"].fillna(0) % 2  >= 0).all()

    if((df[df["Use By Date"] >= date_today]).count < 1):
        return 'Nothing in the fridge to consume'
    elif (is_measure_unit_correct is False):
        return 'Invalid item measurement unit in the file'
    elif (is_quantity_correct is False):
        return 'Invalid item quantity in the file'
    else:
        return df