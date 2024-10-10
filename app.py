from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_graph', methods=['POST'])
def generate_graph():
    currency = request.form['currency']
    year = int(request.form['year'])
    duration = request.form['duration']
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    # Simulated data for demonstration (replace this with actual data loading logic)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    rates = [73 + (i % 10) * 0.1 for i in range(len(dates))]  # Example rates

    df = pd.DataFrame({'Date': dates, 'Rate': rates})
    df['Date'] = pd.to_datetime(df['Date'])

    # Find highest and lowest rates
    highest_rate = df['Rate'].max()
    lowest_rate = df['Rate'].min()
    highest_date = df.loc[df['Rate'] == highest_rate, 'Date'].dt.strftime('%Y-%m-%d').values[0]
    lowest_date = df.loc[df['Rate'] == lowest_rate, 'Date'].dt.strftime('%Y-%m-%d').values[0]

    # Generate the graph
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Rate'], marker='o', color='blue')
    plt.title(f'Exchange Rate of {currency} vs USD', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Exchange Rate', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the graph to a static directory
    graph_path = os.path.join('static', 'graph.png')
    plt.savefig(graph_path)
    plt.close()

    return render_template('graph.html', currency=currency, 
                           highest_rate=highest_rate, highest_date=highest_date, 
                           lowest_rate=lowest_rate, lowest_date=lowest_date)

if __name__ == '__main__':
    # Create the static directory if it doesn't exist
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)
