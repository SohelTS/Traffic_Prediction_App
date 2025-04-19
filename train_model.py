import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv('Dataset.csv', dayfirst=True)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Month'] = df['Date'].dt.month
df['DayOfMonth'] = df['Date'].dt.day


df = pd.get_dummies(df, columns=['Zone'], prefix='Zone')


feature_cols = ['CodedDay', 'Temperature', 'Weather', 'Month', 'DayOfMonth'] + \
               [c for c in df.columns if c.startswith('Zone_')]
X = df[feature_cols]
y = df['Traffic']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_scaled, y_train)


joblib.dump(rf, 'best_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(feature_cols, 'features.pkl')
print("Training complete. Artifacts saved: best_model.pkl, scaler.pkl, features.pkl")
