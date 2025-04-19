from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')
feature_names = joblib.load('features.pkl')

def predict_traffic(coded_day, temp, weather, month, day_of_month, zone):
    
    input_dict = {f: 0 for f in feature_names}

    
    input_dict['CodedDay']   = coded_day
    input_dict['Temperature'] = temp
    input_dict['Weather']     = weather
    input_dict['Month']       = month
    input_dict['DayOfMonth']  = day_of_month

   
    zone_col = f'Zone_{zone}'
    if zone_col in input_dict:
        input_dict[zone_col] = 1


    df = pd.DataFrame([input_dict])
    df_scaled = scaler.transform(df)
    prediction = model.predict(df_scaled)[0]
    return int(prediction)

def get_traffic_description(level):
    descriptions = {
        1: "Very Low Traffic",
        2: "Low Traffic",
        3: "Moderate Traffic",
        4: "High Traffic",
        5: "Very High Traffic"
    }
    return descriptions.get(level, "Unknown")

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None
    traffic_description = None 
    
    form_data = {
        'coded_day': '',
        'temperature': '',
        'weather': '',
        'month': '',
        'day_of_month': '',
        'zone': '',
        'source': '',
        'destination': ''
    }

    if request.method == 'POST':
        try:
            cd = int(request.form['coded_day'])
            tp = float(request.form['temperature'])
            wt = int(request.form['weather'])
            mo = int(request.form['month'])
            dom = int(request.form['day_of_month'])
            zn = int(request.form['zone'])

            form_data = {
                'coded_day': cd,
                'temperature': tp,
                'weather': wt,
                'month': mo,
                'day_of_month': dom,
                'zone': zn,
                'source': request.form.get('source', ''),
                'destination': request.form.get('destination', '')
            }

            prediction = predict_traffic(cd, tp, wt, mo, dom, zn)
            traffic_description = get_traffic_description(prediction) 
        except Exception as e:
            error = f"⚠️ Invalid input: {e}"

   
    return render_template('index.html', prediction=prediction, description=traffic_description, error=error, form_data=form_data)


if __name__ == '__main__':
    app.run(debug=True)
