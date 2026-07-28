import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Intelligence Dashboard",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    """
    <style>

    .main {
        background: linear-gradient(
            135deg,
            #f8fafc,
            #e2e8f0
        );
    }

    h1 {
        color: #2563eb;
        text-align: center;
        font-size: 45px;
    }

    h2, h3 {
        color: #1e293b;
    }

    .metric-card {
        background: rgba(255,255,255,0.8);
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }

    .metric-card h2 {
        color: #2563eb;
    }

    .metric-card p {
        color:#334155;
        font-size:25px;
        font-weight:bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv(
        "data/processed/customer_clv.csv"
    )


df = load_data()


# -----------------------------
# Header
# -----------------------------
st.title("🚀 Customer Intelligence & CLV Dashboard")

st.markdown(
    """
    <h3 style='text-align:center;color:#94a3b8'>
    AI-powered Customer Segmentation and Lifetime Value Analytics
    </h3>
    """,
    unsafe_allow_html=True
)


st.divider()


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🎯 Analytics Controls")


cluster_filter = st.sidebar.multiselect(
    "Select Customer Segments",
    sorted(df["Cluster"].unique()),
    default=sorted(df["Cluster"].unique())
)


value_filter = st.sidebar.multiselect(
    "Customer Value Category",
    df["Customer_Value"].unique(),
    default=df["Customer_Value"].unique()
)


filtered_df = df[
    (df["Cluster"].isin(cluster_filter))
    &
    (df["Customer_Value"].isin(value_filter))
]


# -----------------------------
# KPI Cards
# -----------------------------

c1,c2,c3 = st.columns(3)


with c1:
    st.markdown(
        f"""
        <div class='metric-card'>
        <h2>👥 Customers</h2>
        <p>{len(filtered_df):,}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


with c2:
    st.markdown(
        f"""
        <div class='metric-card'>
        <h2>💰 Revenue</h2>
        <p>${filtered_df['Monetary'].sum():,.0f}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


with c3:
    st.markdown(
        f"""
        <div class='metric-card'>
        <h2>💎 Avg CLV</h2>
        <p>${filtered_df['CLV'].mean():,.0f}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# -----------------------------
# Charts
# -----------------------------

col1,col2 = st.columns(2)


with col1:

    st.subheader("🌌 Customer Segments")

    fig = px.pie(
        filtered_df,
        names="Cluster",
        title="Customer Distribution",
        hole=0.45
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


with col2:

    st.subheader("💎 Customer Value")

    fig = px.bar(
        filtered_df["Customer_Value"]
        .value_counts()
        .reset_index(),
        x="Customer_Value",
        y="count",
        title="Value Category Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# -----------------------------
# CLV Analysis
# -----------------------------

st.subheader("📈 CLV Distribution")


fig = px.histogram(
    filtered_df,
    x="CLV",
    nbins=30,
    title="Customer Lifetime Value Spread"
)


st.plotly_chart(
    fig,
    use_container_width=True
)



# -----------------------------
# Top Customers
# -----------------------------

st.subheader("🏆 Premium Customers")


top_customers = (
    filtered_df
    .sort_values(
        "CLV",
        ascending=False
    )
    .head(10)
)


st.dataframe(
    top_customers,
    use_container_width=True
)


# -----------------------------
# Download
# -----------------------------

csv = filtered_df.to_csv(index=False)


st.download_button(
    "📥 Download Customer Report",
    csv,
    "customer_clv_report.csv",
    "text/csv"
)