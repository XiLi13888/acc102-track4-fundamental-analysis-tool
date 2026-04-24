\# Listed Company Fundamental \& Investment Risk Analyzer



This is an interactive investment analysis tool developed for the ACC102 course, which is part of the Economics and Finance programme at Xi’an Jiaotong-Liverpool University. The main purpose of this tool is to turn the fundamental investment analysis framework we learned in the course into something practical and easy to use for ordinary retail investors. It helps users quickly figure out whether a listed company’s stock is worth buying, without needing professional financial knowledge or coding skills.



\## Data Source

All data used in the tool is fetched from Yahoo Finance through the yfinance Python library, as of April 22, 2026. The data includes real-time market valuation metrics and the latest financial statement data from the companies’ official SEC filings—all of which is public and reliable enough for investment reference.



\## Target Users

The tool is mainly for non-professional individual retail investors. If you want to do a quick, reliable fundamental analysis before making a stock investment decision, or if you need a simple, no-code way to check a company’s financial health and investment risks, this tool is designed for you.



\## Core Features

\- Get key equity valuation metrics like market cap, turnover rate, P/E ratio, and P/B ratio with just one click.

\- Visual chart showing the stock’s 1-year historical price trend (easy to understand performance and volatility).

\- Quantitative downside risk warning function: assesses delisting and financial risks based on set rules to avoid high-risk stocks.

\- Automatically calculates core financial performance ratios (net profit margin, ROA, ROE, debt-to-asset ratio) to evaluate profitability and financial stability.

\- Compare the target company with a custom peer group average (avoids misjudgments from isolated ratio numbers).

\- No-code \& user-friendly interface: no coding experience or professional finance background required.



\## Repository Structure

The main folder is ACC102-Track4-Investment-Analyzer, which contains three files:

\- `app.py`: Core Streamlit application code

\- `requirements.txt`: All dependency packages with locked versions (ensures reproducibility)

\- `README.md`: Project documentation



\## How to Run Locally

1\. Clone this repository to your local machine.

2\. Install all required dependencies in your terminal:

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

&#x20;  ```

3\. Run the application:

&#x20;  ```bash

&#x20;  streamlit run app.py

&#x20;  ```

4\. The app will automatically open in your default browser.



\## Demo Video

\[XJTLU Mediasite Demo](https://video.xjtlu.edu.cn/Mediasite/Play/2769ada4bd4641d5b2f21c5cb86cdb301d)



\## Limitations

\- The risk assessment rules are simplified for basic investor screening; data may have short delays (depends on Yahoo Finance’s update frequency).

\- Only suitable for fundamental-focused value investors (not for short-term traders relying on technical analysis/intraday trading strategies).

\- Provides standardized fundamental analysis as reference only: cannot guarantee high-quality stock picks, nor replace independent judgment/due diligence before investing.



\## Future Improvements

\- Add a discounted cash flow (DCF) valuation module (core method in corporate finance and security analysis).

\- Add multi-year financial health trend analysis function.

\- Integrate basic technical indicators (accommodate users with different investment styles).

\- Add PDF analysis report export function.



\## Tech Stack

\- Python

\- Streamlit

\- yfinance

\- pandas

\- matplotlib



\## Disclaimer

This project is for educational use (as part of the ACC102 course) and investment reference only.

