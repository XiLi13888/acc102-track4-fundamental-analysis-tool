  Listed Company Fundamental & Investment Risk Analyzer

This is an interactive investment analysis tool developed for the ACC102 course, which is part of the Economics and Finance programme at Xi’an Jiaotong-Liverpool University. The main purpose of this tool is to turn the fundamental investment analysis framework we learned in the course into something practical and easy to use for ordinary retail investors. It helps users quickly figure out whether a listed company’s stock is worth buying, without needing professional financial knowledge or coding skills.

All data used in the tool is fetched from Yahoo Finance through the yfinance Python library, as of April 22, 2026. The data includes real-time market valuation metrics and the latest financial statement data from the companies’ official SEC filings—all of which is public and reliable enough for investment reference.

The tool is mainly for non-professional individual retail investors. If you want to do a quick, reliable fundamental analysis before making a stock investment decision, or if you need a simple, no-code way to check a company’s financial health and investment risks, this tool is designed for you.

Here are the core features of the tool. You can get key equity valuation metrics like market cap, turnover rate, P/E ratio, and P/B ratio with just one click. There’s also a visual chart showing the stock’s 1-year historical price trend, so you can easily understand its performance and volatility. We’ve added a quantitative downside risk warning function too—based on set rules, it assesses delisting and financial risks to help you avoid high-risk stocks. The tool automatically calculates core financial performance ratios, such as net profit margin, ROA, ROE, and debt-to-asset ratio, to help you evaluate a company’s profitability and financial stability. You can also compare the target company with a custom peer group average, which helps avoid misjudgments from looking at isolated ratio numbers. Most importantly, it’s a no-code tool with a user-friendly interface—you don’t need any coding experience or professional finance background to use it.

The repository structure is simple and straightforward. The main folder is ACC102-Track4-Investment-Analyzer, which contains three files: app.py is the core Streamlit application code, requirements.txt lists all the dependency packages with locked versions to ensure reproducibility, and this README.md file serves as the project documentation.

If you want to run the tool locally, follow these steps. First, clone this repository to your local machine. Then, install all the required dependencies by running the command “pip install -r requirements.txt” in your terminal. After that, run the application with “streamlit run app.py”—it will automatically open in your default browser.

Demo Video:https://video.xjtlu.edu.cn/Mediasite/Play/2769ada4bd4641d5b2f21c5cb86cdb301d

 It’s important to note the tool’s limitations. First, the risk assessment rules are simplified for basic investor screening, and the data depends on Yahoo Finance’s update frequency, so there may be a short delay. Second, this tool is only for fundamental-focused value investors—it’s not suitable for short-term traders who rely on technical analysis or intraday trading strategies. Third, the tool only provides standardized fundamental analysis as a reference; it can’t guarantee that you’ll pick high-quality stocks, nor can it replace your own independent judgment and due diligence before investing.

For future improvements, we plan to add a discounted cash flow (DCF) valuation module, which is a core method in corporate finance and security analysis. We also want to add a multi-year financial health trend analysis function, integrate basic technical indicators to accommodate users with different investment styles, and add a PDF analysis report export function.

The tools and libraries used in this project include Python, Streamlit, yfinance, pandas, and matplotlib.
This project is for educational use (as part of the ACC102 course) and investment reference only.