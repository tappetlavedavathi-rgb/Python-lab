# AI in Finance and Banking
# Python Fundamentals Lab Project

# --------------------------------------------------
# 1. Transaction Data
# --------------------------------------------------

# List of dictionaries containing 8 fictional transactions
transactions = [
    {"id": "TXN001", "amount": 4500, "city": "Visakhapatnam"},
    {"id": "TXN002", "amount": 12500, "city": "Hyderabad"},
    {"id": "TXN003", "amount": 7800, "city": "Vijayawada"},
    {"id": "TXN004", "amount": 15000, "city": "Bengaluru"},
    {"id": "TXN005", "amount": 3200, "city": "Chennai"},
    {"id": "TXN006", "amount": 9500, "city": "Visakhapatnam"},
    {"id": "TXN007", "amount": 18000, "city": "Hyderabad"},
    {"id": "TXN008", "amount": 6200, "city": "Vijayawada"}
]

# Sample monitoring limit used for this project
monitoring_limit = 10000


# --------------------------------------------------
# 2. Function to Process Transactions
# --------------------------------------------------

def process_transactions(transactions, limit):

    # Counters for normal and flagged transactions
    normal_count = 0
    flagged_count = 0

    # Empty string to store HTML table rows
    rows = ""

    # Check each transaction one by one
    for transaction in transactions:

        # Check whether the amount is above the monitoring limit
        if transaction["amount"] > limit:
            status = "Suspicious - Review"
            reason = "Amount crossed the monitoring limit."

            # Increase flagged transaction counter
            flagged_count += 1

            # CSS class for highlighted row
            row_class = "flagged"

        else:
            status = "Normal"
            reason = "-"

            # Increase normal transaction counter
            normal_count += 1

            # CSS class for normal row
            row_class = "normal"

        # Create one HTML table row
        rows += f"""
        <tr class="{row_class}">
            <td>{transaction["id"]}</td>
            <td>₹{transaction["amount"]:,}</td>
            <td>{transaction["city"]}</td>
            <td>{status}</td>
            <td>{reason}</td>
        </tr>
        """

    # Return the processed data
    return rows, normal_count, flagged_count


# Call the function
table_rows, normal_count, flagged_count = process_transactions(
    transactions, monitoring_limit
)


# --------------------------------------------------
# 3. Calculate Summary Information
# --------------------------------------------------

# Count total number of transactions
total_transactions = len(transactions)

# Calculate total transaction amount
total_amount = sum(transaction["amount"] for transaction in transactions)

# Find the number of different cities
cities = set(transaction["city"] for transaction in transactions)
cities_count = len(cities)


# --------------------------------------------------
# 4. Create HTML Webpage
# --------------------------------------------------

html = f"""
<!DOCTYPE html>
<html>

<head>
    <title>AI in Finance & Banking</title>

    <style>

        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            background-color: #f4f7fb;
            color: #222;
        }}

        header {{
            background-color: #173b63;
            color: white;
            text-align: center;
            padding: 30px;
        }}

        header h1 {{
            margin: 0;
            font-size: 32px;
        }}

        header p {{
            font-size: 16px;
        }}

        .container {{
            width: 90%;
            max-width: 1100px;
            margin: 30px auto;
        }}

        .section {{
            background-color: white;
            padding: 25px;
            margin-bottom: 25px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }}

        .dashboard {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 15px;
        }}

        .card {{
            background-color: #eaf2f8;
            padding: 20px;
            text-align: center;
            border-radius: 10px;
        }}

        .card h3 {{
            margin-bottom: 10px;
            color: #173b63;
        }}

        .card p {{
            font-size: 22px;
            font-weight: bold;
            margin: 0;
        }}

        .ai-boxes {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }}

        .ai-box {{
            background-color: #f7f9fc;
            padding: 20px;
            border-left: 5px solid #173b63;
            border-radius: 8px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }}

        th {{
            background-color: #173b63;
            color: white;
            padding: 12px;
        }}

        td {{
            padding: 12px;
            text-align: center;
            border-bottom: 1px solid #ddd;
        }}

        .normal {{
            background-color: #f8fff8;
        }}

        .flagged {{
            background-color: #fff1f1;
        }}

        .flow {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .flow-box {{
            background-color: #eaf2f8;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
        }}

        .arrow {{
            font-size: 22px;
        }}

        footer {{
            background-color: #173b63;
            color: white;
            text-align: center;
            padding: 18px;
            margin-top: 30px;
        }}

    </style>
</head>


<body>

    <!-- Header -->
    <header>
        <h1>AI in Finance & Banking</h1>
        <p>Understanding how AI supports modern financial services</p>
    </header>


    <div class="container">

        <!-- Introduction -->
        <div class="section">

            <h2>Introduction</h2>

            <p>
                Artificial Intelligence is used in finance and banking to
                analyse large amounts of data, identify unusual transaction
                patterns, support credit assessment and provide useful
                information for financial decision-making.
            </p>

        </div>


        <!-- Dashboard -->
        <div class="section">

            <h2>Transaction Dashboard</h2>

            <div class="dashboard">

                <div class="card">
                    <h3>Total Transactions</h3>
                    <p>{total_transactions}</p>
                </div>

                <div class="card">
                    <h3>Total Amount</h3>
                    <p>₹{total_amount:,}</p>
                </div>

                <div class="card">
                    <h3>Cities Covered</h3>
                    <p>{cities_count}</p>
                </div>

                <div class="card">
                    <h3>Normal</h3>
                    <p>{normal_count}</p>
                </div>

                <div class="card">
                    <h3>Flagged for Review</h3>
                    <p>{flagged_count}</p>
                </div>

            </div>

        </div>


        <!-- How AI Helps -->
        <div class="section">

            <h2>How AI Helps in Finance & Banking</h2>

            <div class="ai-boxes">

                <div class="ai-box">
                    <h3>Fraud Detection</h3>

                    <p>
                        AI can analyse transaction patterns and identify
                        unusual activity that may need further review.
                    </p>
                </div>


                <div class="ai-box">
                    <h3>Credit Scoring</h3>

                    <p>
                        AI can analyse financial and credit-related information
                        to support credit and loan assessment.
                    </p>
                </div>


                <div class="ai-box">
                    <h3>Trading Support</h3>

                    <p>
                        AI can analyse large amounts of market data and
                        identify patterns that can support financial analysis.
                    </p>
                </div>

            </div>

        </div>


        <!-- Transaction Monitor -->
        <div class="section">

            <h2>Transaction Monitor</h2>

            <p>
                Monitoring Limit:
                <strong>₹{monitoring_limit:,}</strong>
            </p>

            <p>
                Transactions above this sample limit are marked
                <strong>Suspicious - Review</strong>.
                This does not mean that the transaction is confirmed fraud.
            </p>


            <table>

                <tr>
                    <th>Transaction ID</th>
                    <th>Amount</th>
                    <th>City</th>
                    <th>Status</th>
                    <th>Why Flagged?</th>
                </tr>

                {table_rows}

            </table>

        </div>


        <!-- Monitoring Summary -->
        <div class="section">

            <h2>Monitoring Summary</h2>

            <p>
                Total Transactions:
                <strong>{total_transactions}</strong>
            </p>

            <p>
                Normal Transactions:
                <strong>{normal_count}</strong>
            </p>

            <p>
                Flagged Transactions:
                <strong>{flagged_count}</strong>
            </p>

            <p>
                Total Transaction Amount:
                <strong>₹{total_amount:,}</strong>
            </p>

        </div>


        <!-- System Flow -->
        <div class="section">

            <h2>How the System Works</h2>

            <div class="flow">

                <div class="flow-box">
                    Transaction Data
                </div>

                <div class="arrow">→</div>

                <div class="flow-box">
                    Python Processing
                </div>

                <div class="arrow">→</div>

                <div class="flow-box">
                    Check Monitoring Limit
                </div>

                <div class="arrow">→</div>

                <div class="flow-box">
                    Normal / Flagged for Review
                </div>

                <div class="arrow">→</div>

                <div class="flow-box">
                    Generate Webpage
                </div>

            </div>

        </div>

    </div>


    <!-- Footer -->
    <footer>
        Created using Python
    </footer>

</body>
</html>
"""


# --------------------------------------------------
# 5. Save the Webpage
# --------------------------------------------------

# Create index.html and write the generated webpage into it
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html)


# Display the result in the VS Code terminal
print("Webpage created successfully!")
print("File name: index.html")
print("Total transactions:", total_transactions)
print("Normal transactions:", normal_count)
print("Flagged transactions:", flagged_count)
print("Total transaction amount: ₹", total_amount)