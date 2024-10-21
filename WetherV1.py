import numpy as np
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import messagebox

# Function to collect weather data from the user
def collect_weather_data(entries):
    data = []
    try:
        for i in range(7):
            temp = float(entries[f"temp_{i}"].get())
            humidity = float(entries[f"humidity_{i}"].get())
            data.append([temp, humidity])
        return np.array(data)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for temperature and humidity.")
        return None

# Function to predict weather for the next 7 days
def predict_weather(data):
    X = np.arange(1, 8).reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, data)
    future_days = np.arange(8, 15).reshape(-1, 1)
    predictions = model.predict(future_days)
    return predictions

# Function to handle the prediction process
def handle_predict(entries, result_label):
    data = collect_weather_data(entries)
    if data is not None:
        predictions = predict_weather(data)
        result_text = "Weather predictions for the next 7 days:\n"
        for i, prediction in enumerate(predictions, start=1):
            result_text += f"Day {i}: Temperature: {prediction[0]:.2f}, Humidity: {prediction[1]:.2f}\n"
        result_label.config(text=result_text)

# Main function to create the GUI
def main():
    root = tk.Tk()
    root.title("Weather Prediction")

    entries = {}
    for i in range(7):
        tk.Label(root, text=f"Day {i+1} Temperature:").grid(row=i, column=0)
        entries[f"temp_{i}"] = tk.Entry(root)
        entries[f"temp_{i}"].grid(row=i, column=1)

        tk.Label(root, text=f"Day {i+1} Humidity:").grid(row=i, column=2)
        entries[f"humidity_{i}"] = tk.Entry(root)
        entries[f"humidity_{i}"].grid(row=i, column=3)

    result_label = tk.Label(root, text="", justify=tk.LEFT)
    result_label.grid(row=8, column=0, columnspan=4)

    predict_button = tk.Button(root, text="Predict Weather", command=lambda: handle_predict(entries, result_label))
    predict_button.grid(row=7, column=0, columnspan=4)

    root.mainloop()

if __name__ == "__main__":
    main()