import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import datetime
# import multitasking 

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
from tensorflow.keras.optimizers import Adam

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Multi-Stock Prediction Dashboard",
    layout="wide"
)

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------
st.sidebar.title("📊 Stock Selection")

ticker = st.sidebar.selectbox(
    "Choose Company",
    ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
)

lookback_days = st.sidebar.slider(
    "Lookback Days",
    min_value=30,
    max_value=120,
    value=60
)

forecast_horizon = st.sidebar.selectbox(
    "Forecast Horizon (days)",
    [1, 2]
)

st.sidebar.markdown("🔄 Auto-refresh every 30s")

# ----------------------------------------------------
# TITLE
# ----------------------------------------------------
st.title("📈 Multi-Stock Real-Time Prediction Dashboard")

# ----------------------------------------------------
# DATA FETCHING
# ----------------------------------------------------
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=365 * 10)

df = yf.download(ticker, start=start_date, end=end_date)

if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

features = ["Open", "High", "Low", "Close", "Volume"]
data = df[features].values

# ----------------------------------------------------
# DATA PREPARATION FUNCTION
# ----------------------------------------------------
def create_dataset(data, time_step=60):
    X, y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:i + time_step])
        y.append(data[i + time_step, [0, 3]])  # Open & Close
    return np.array(X), np.array(y)

# ----------------------------------------------------
# TRAIN GRU MODEL
# ----------------------------------------------------
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

X, y = create_dataset(scaled_data, lookback_days)
X = X.reshape(X.shape[0], X.shape[1], X.shape[2])

with st.spinner("Training GRU model..."):
    model = Sequential()
    model.add(GRU(64, return_sequences=True,
                  input_shape=(lookback_days, X.shape[2])))
    model.add(GRU(64))
    model.add(Dense(2))  # Open & Close

    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss="mean_squared_error"
    )

    model.fit(X, y, epochs=5, batch_size=32, verbose=0)

# ----------------------------------------------------
# PREDICTION
# ----------------------------------------------------
last_sequence = scaled_data[-lookback_days:]
last_sequence = last_sequence.reshape(1, lookback_days, 5)

pred_scaled = model.predict(last_sequence)

# inverse scaling
dummy = np.zeros((1, 5))
dummy[0, 0] = pred_scaled[0, 0]
dummy[0, 3] = pred_scaled[0, 1]
predicted_prices = scaler.inverse_transform(dummy)

next_open = predicted_prices[0, 0]
next_close = predicted_prices[0, 3]



# ----------------------------------------------------
# OUTPUT DATAFRAME
# ----------------------------------------------------
output_df = pd.DataFrame({
    "Date": [df.index[-1].date()],
    "Last Open": [float(df["Open"].iloc[-1])],
    "Last Close": [float(df["Close"].iloc[-1])],
    "Predicted Next Open": [next_open],
    "Predicted Next Close": [next_close]
})



# ----------------------------------------------------
# DASHBOARD METRICS
# ----------------------------------------------------
st.subheader(f"🎯 {ticker} Predictions")
tab1, tab2, tab3 = st.tabs([
    "📊 Real-time Predictions",
    "📈 Analysis Charts",
    "🧠 Model & Data"
])

with tab1:
    st.subheader(f"🎯 {ticker} Predictions")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Last Close", f"${float(df['Close'].iloc[-1]):.2f}")
    col2.metric("Today Open", f"${float(df['Open'].iloc[-1]):.2f}")
    col3.metric("Next Open", f"${next_open:.2f}")
    col4.metric("Next Close", f"${next_close:.2f}")

    st.subheader("📋 Prediction Output Table")
    st.dataframe(output_df, use_container_width=True)


# ----------------------------------------------------
# CHART
# ----------------------------------------------------
with tab2:
    st.subheader("📊 Open vs Close Price")

    open_close_df = df[["Open", "Close"]].tail(200)
    st.line_chart(open_close_df)

    st.subheader("📊 Volume Trend")
    st.line_chart(df["Volume"].tail(200))

    st.subheader("📈 Daily Returns (%)")

    df["Daily Return %"] = df["Close"].pct_change() * 100
    st.line_chart(df["Daily Return %"].tail(200))


with tab3:
    st.subheader("🧠 GRU Model Details")

    st.markdown(f"""
    **Model Type:** Gated Recurrent Unit (GRU)  
    **Input Features:** Open, High, Low, Close, Volume  
    **Lookback Window:** Last {lookback_days} days  
    **Output:** Next Day Open & Close Price  
    **Loss Function:** Mean Squared Error  
    **Optimizer:** Adam  
    """)

    st.subheader("📊 Last 10 days Data")
    st.dataframe(df.tail(10), use_container_width=True)

# ----------------------------------------------------
# FORECAST INFO 
# ----------------------------------------------------
st.info(
    "This GRU model uses the last "
    f"{lookback_days} days of Open, High, Low, Close, and Volume "
    "to predict the next day's Open and Close prices."
)


