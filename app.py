import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(
    page_title="Listed Company Financial & Risk Analyzer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------
# Header & Project Introduction
# --------------------------
st.title("Listed Company Financial & Risk Analyzer")
st.subheader("ACC102 Track 4 | Interactive Data Analysis Tool")
st.markdown("""
This tool integrates real-time stock market data, core accounting ratio calculation, peer benchmarking, and delisting risk assessment for accounting & finance learners.
It solves the pain point of scattered data in traditional trading platforms, providing a one-stop educational analysis solution.
""")

# --------------------------
# User Input Section
# --------------------------
with st.sidebar:
    st.header("Analysis Settings")
    ticker = st.text_input("Enter Stock Ticker (e.g. AAPL, MSFT, TSLA)", value="AAPL")
    benchmark_tickers = st.text_input(
        "Peer Benchmark Tickers (comma separated)",
        value="MSFT, GOOGL, AMZN"
    )
    st.divider()
    run_analysis = st.button("Run Full Analysis", type="primary", use_container_width=True)

# --------------------------
# Core Analysis Logic
# --------------------------
if run_analysis:
    # Error handling for invalid tickers
    try:
        # 1. Load target company data
        with st.spinner("Loading target company data..."):
            target_stock = yf.Ticker(ticker)
            target_info = target_stock.info
            # Validate data availability
            if not target_info.get("symbol"):
                st.error("Invalid ticker symbol. Please check and try again.")
                st.stop()

        # 2. Load peer benchmark data
        with st.spinner("Loading peer benchmark data..."):
            peer_list = [t.strip() for t in benchmark_tickers.split(",")]
            peer_data = []
            for peer in peer_list:
                try:
                    peer_stock = yf.Ticker(peer)
                    peer_info = peer_stock.info
                    peer_data.append({
                        "ticker": peer,
                        "pe": peer_info.get("trailingPE", 0),
                        "pb": peer_info.get("priceToBook", 0),
                        "net_margin": peer_info.get("netIncomeToCommon", 0) / peer_info.get("totalRevenue", 1) if peer_info.get("totalRevenue", 0) > 0 else 0,
                        "roe": peer_info.get("returnOnEquity", 0),
                        "debt_ratio": peer_info.get("totalLiabilities", 0) / peer_info.get("totalAssets", 1) if peer_info.get("totalAssets", 0) > 0 else 0
                    })
                except:
                    continue
            peer_df = pd.DataFrame(peer_data)
            industry_avg = peer_df.mean(numeric_only=True)

        # --------------------------
        # Section 1: Company & Stock Basic Info
        # --------------------------
        st.divider()
        st.subheader("📌 Company & Core Market Indicators")
        # Extract core metrics
        company_name = target_info.get("longName", "N/A")
        sector = target_info.get("sector", "N/A")
        country = target_info.get("country", "N/A")
        currency = target_info.get("currency", "USD")
        market_cap = target_info.get("marketCap", 0)
        volume = target_info.get("volume", 0)
        shares_outstanding = target_info.get("sharesOutstanding", 1)
        turnover_rate = volume / shares_outstanding if shares_outstanding > 0 else 0
        pe_ratio = target_info.get("trailingPE", 0)
        pb_ratio = target_info.get("priceToBook", 0)

        # Layout in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Company Name", company_name)
            st.metric("Sector", sector)
            st.metric("Country", country)
        with col2:
            st.metric("Market Capitalization", f"${market_cap:,.0f}")
            st.metric("Daily Turnover Rate", f"{turnover_rate:.2%}")
            st.metric("Trading Currency", currency)
        with col3:
            st.metric("Trailing P/E Ratio", f"{pe_ratio:.2f}" if pe_ratio != 0 else "N/A")
            st.metric("Price-to-Book (P/B) Ratio", f"{pb_ratio:.2f}" if pb_ratio != 0 else "N/A")

        # Historical Price Chart
        st.subheader("📈 1-Year Historical Price Trend")
        hist_data = target_stock.history(period="1y")
        st.line_chart(hist_data["Close"], use_container_width=True)

        # --------------------------
        # Section 2: Delisting Risk Assessment
        # --------------------------
        st.divider()
        st.subheader("⚠️ Delisting Risk Assessment")
        risk_score = 0
        risk_factors = []

        # Risk rule set (academic standard for educational use)
        if market_cap < 2_000_000_000:
            risk_score += 3
            risk_factors.append("Small market capitalization (below $2B)")
        if pe_ratio < 0 or pe_ratio > 100:
            risk_score += 2
            risk_factors.append("Abnormal P/E ratio (negative or over 100)")
        if pb_ratio > 20:
            risk_score += 2
            risk_factors.append("Extremely high P/B ratio (over 20)")
        if target_info.get("operatingCashflow", 0) < 0:
            risk_score += 2
            risk_factors.append("Negative operating cash flow")

        # Risk level classification
        if risk_score >= 5:
            risk_level = "High Risk"
            risk_color = "red"
        elif 2 <= risk_score < 5:
            risk_level = "Medium Risk"
            risk_color = "orange"
        else:
            risk_level = "Low Risk"
            risk_color = "green"
            risk_factors.append("Stable core financial indicators")

        st.metric("Overall Risk Level", risk_level)
        st.markdown(f"**Risk Factors:** {', '.join(risk_factors)}")

        # --------------------------
        # Section 3: Financial Ratio Analysis & Peer Benchmarking
        # --------------------------
        st.divider()
        st.subheader("📊 Core Accounting Ratios & Peer Benchmarking")
        st.markdown("*Comparison with industry peer average*")

        # Calculate core financial ratios
        total_revenue = target_info.get("totalRevenue", 0)
        net_income = target_info.get("netIncomeToCommon", 0)
        total_assets = target_info.get("totalAssets", 0)
        total_liabilities = target_info.get("totalLiabilities", 0)
        total_equity = target_info.get("stockholdersEquity", 1)

        net_profit_margin = net_income / total_revenue if total_revenue > 0 else 0
        roa = net_income / total_assets if total_assets > 0 else 0
        roe = net_income / total_equity if total_equity > 0 else 0
        debt_to_asset_ratio = total_liabilities / total_assets if total_assets > 0 else 0

        # Comparison table
        comparison_df = pd.DataFrame({
            "Metric": ["Net Profit Margin", "Return on Assets (ROA)", "Return on Equity (ROE)", "Debt-to-Asset Ratio"],
            "Target Company": [f"{net_profit_margin:.1%}", f"{roa:.1%}", f"{roe:.1%}", f"{debt_to_asset_ratio:.1%}"],
            "Industry Peer Average": [
                f"{industry_avg['net_margin']:.1%}",
                f"{industry_avg['roe']:.1%}",
                f"{industry_avg['roe']:.1%}",
                f"{industry_avg['debt_ratio']:.1%}"
            ]
        })
        st.dataframe(comparison_df, use_container_width=True, hide_index=True)

        # Ratio interpretation
        st.subheader("📝 Ratio Interpretation")
        interpretation_col1, interpretation_col2 = st.columns(2)
        with interpretation_col1:
            st.markdown(f"- **Net Profit Margin**: {net_profit_margin:.1%} vs industry average {industry_avg['net_margin']:.1%}")
            st.markdown(f"- **ROA**: {roa:.1%} vs industry average {industry_avg['roe']:.1%}")
        with interpretation_col2:
            st.markdown(f"- **ROE**: {roe:.1%} vs industry average {industry_avg['roe']:.1%}")
            st.markdown(f"- **Debt-to-Asset Ratio**: {debt_to_asset_ratio:.1%} vs industry average {industry_avg['debt_ratio']:.1%}")

        st.success("✅ Full analysis completed successfully. All workflow runs as expected.")

    except Exception as e:
        st.error(f"Analysis failed. Error: {str(e)}. Please check the ticker symbols and try again.")