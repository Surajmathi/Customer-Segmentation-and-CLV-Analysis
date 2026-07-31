import streamlit as st
import pandas as pd
from PIL import Image
from utils import load_data
from components import kpi_card

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Global Superstore Analytics",
    page_icon="assets/logo.png" ,
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# LOAD CSS
# -------------------------------------------------
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
df = load_data()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("📊 Navigation")

st.sidebar.markdown("---")

cluster = st.sidebar.multiselect(
    "Customer Cluster",
    sorted(df["Cluster"].unique()),
    default=sorted(df["Cluster"].unique())
)

customer_value = st.sidebar.multiselect(
    "Customer Value",
    sorted(df["Customer_Value"].unique()),
    default=sorted(df["Customer_Value"].unique())
)

search = st.sidebar.text_input(
    "Search Customer ID"
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Executive Customer Intelligence Portal"
)

# -------------------------------------------------
# FILTER DATA
# -------------------------------------------------
filtered = df[
    (df["Cluster"].isin(cluster)) &
    (df["Customer_Value"].isin(customer_value))
]

if search:
    filtered = filtered[
        filtered["customer_id"]
        .astype(str)
        .str.contains(search)
    ]

# -------------------------------------------------
# HEADER
# -------------------------------------------------
banner = Image.open("assets/banner.png")

st.image(
    banner,
    use_container_width=True
)

st.markdown(
    """
<div class="dashboard-title">
Global Superstore Analytics Dashboard
</div>

<div class="dashboard-subtitle">
Executive Customer Intelligence Portal
</div>
""",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------
# KPI VALUES
# -------------------------------------------------

total_customers = len(filtered)

total_revenue = filtered["Monetary"].sum()

average_clv = filtered["CLV"].mean()

segments = filtered["Cluster"].nunique()

# -------------------------------------------------
# KPI ROW
# -------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    kpi_card(
        "TOTAL CUSTOMERS",
        f"{total_customers:,}"
    )

with c2:
    kpi_card(
        "TOTAL REVENUE",
        f"${total_revenue:,.0f}"
    )

with c3:
    kpi_card(
        "AVERAGE CLV",
        f"${average_clv:,.0f}"
    )

with c4:
    kpi_card(
        "CUSTOMER SEGMENTS",
        segments
    )

st.markdown("---")

st.subheader("📈 Executive Dashboard")

st.info(
    "Interactive business intelligence visualizations will appear below in the next step."
)