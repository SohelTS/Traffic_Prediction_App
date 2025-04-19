# 🚦Traffic_Prediction_App
A research-based practice project where a model of traffic congestion prediction was constructed by using machine learning classification algorithm - random forest and Support Vector  Regression.

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

> ✨ This project demonstrates how day, temperature, zone, and weather can be leveraged to build predictive models for real-world traffic behavior using supervised learning.
