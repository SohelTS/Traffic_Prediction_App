# 🚦Traffic_Prediction_App
Research-based project that builds a traffic congestion prediction system using machine learning algorithms — Random Forest and Support Vector Regression (SVR). The trained model is deployed via a Flask web application that allows users to input parameters like day, weather, temperature, and zone to get real-time traffic level predictions along with descriptive feedback through a clean web interface.

## 📊 About the Dataset

The dataset includes various features recorded over different zones and dates to help predict traffic congestion levels.

- **📅 Date**  
  Records the date in the format **DD/MM/YYYY**.

- **📆 Day**  
  The weekday (e.g., Monday, Tuesday) on which the data was collected. This helps analyze how traffic varies depending on the day of the week.

- **🔢 Coded Day**  
  Weekdays are assigned numeric codes to simplify model input:

  | Day       | Code |
  |-----------|------|
  | Monday    | 1    |
  | Tuesday   | 2    |
  | Wednesday | 3    |
  | Thursday  | 4    |
  | Friday    | 5    |
  | Saturday  | 6    |
  | Sunday    | 7    |

- **🌍 Zone**  
  Indicates the zone number for which traffic data is collected. Each zone considers different **weather conditions** (e.g., humidity, mist, visibility, precipitation) which may affect traffic levels.

- **🌡️ Temperature**  
  The recorded temperature for the corresponding zone and day. Temperature plays a key role in traffic behavior and forecasting.

- **🚗 Traffic (Target Variable)**  
  Traffic congestion is classified into **5 levels** based on the number of cars:

  | Level | Description           |
  |-------|-----------------------|
  | 1     | Less than 5 cars      |
  | 2     | 5 to 15 cars          |
  | 3     | 15 to 30 cars         |
  | 4     | 30 to 50 cars         |
  | 5     | More than 50 cars     |

---

## 📈 Model Performance Comparison

| Model                      | Error (%) | Accuracy (%) |
|---------------------------|-----------|---------------|
| 🔍 Random Forest           | 13.42     | 86.58         |
| 💡 Support Vector Regression (SVR) | 12.16     | 87.84         |

---

## 🌐 Flask Web Application

A lightweight web app built using Flask lets users input prediction parameters through a clean UI and get instant traffic level predictions.

### 🔧 Inputs on the UI:
- Coded Day (1–7)
- Temperature (°C)
- Weather (numeric code)
- Month (1–12)
- Day of the Month (1–31)
- Zone number (1–144)

###  Backend Logic:
- Loads a trained Random Forest model (`best_model.pkl`)
- Applies a `StandardScaler` (`scaler.pkl`) to normalize inputs
- Predicts traffic level (1–5) and maps it to human-readable descriptions like "Low Traffic", "High Traffic", etc.

---

