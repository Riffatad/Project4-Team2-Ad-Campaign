
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.colors as pc

# Set Page Config
st.set_page_config(page_title="Ad Campaign Dashboard", page_icon="📊", layout="wide")

# Load Data
df = pd.read_csv("rf_predictions.csv")

#  Define Category Reference Mapping
reference_data = {
    "Platform": {0: "Facebook", 1: "Google", 2: "Instagram", 3: "LinkedIn", 4: "YouTube"},
    "Content Type": {0: "Carousel", 1: "Image", 2: "Story", 3: "Text", 4: "Video"},
    "Target Age": {0: "18-24", 1: "25-34", 2: "35-44", 3: "45-54", 4: "55+"},
    "Region": {0: "Canada", 1: "Germany", 2: "India", 3: "UK", 4: "US"}
}

#  Sidebar Title
st.sidebar.markdown("## 🔍 Filter Options")

# Sidebar Filters
selected_platforms = st.sidebar.multiselect("🎯 Select Platform(s)", df["Platform"].unique(), default=df["Platform"].unique())
selected_content_types = st.sidebar.multiselect("🎬 Select Content Type(s)", df["Content_Type"].unique(), default=df["Content_Type"].unique())
selected_target_ages = st.sidebar.multiselect("👥 Select Target Age Group", df["Target_Age"].unique(), default=df["Target_Age"].unique())
selected_regions = st.sidebar.multiselect("🌍 Select Region", df["Region"].unique(), default=df["Region"].unique())

#  Apply Filters
filtered_df = df[
    (df["Platform"].isin(selected_platforms)) &
    (df["Content_Type"].isin(selected_content_types)) &
    (df["Target_Age"].isin(selected_target_ages)) &
    (df["Region"].isin(selected_regions))
]

#  Dashboard Title
st.markdown("## 📊 Ad Campaign Performance Dashboard")

# Display Category Reference Table
st.sidebar.markdown("### 🏷️ Category Reference Guide")
st.sidebar.dataframe(pd.DataFrame(reference_data).T, width=300)  # Better formatting

# Display Filtered Data
st.subheader("📌 Filtered Data")
st.dataframe(filtered_df)

# Custom Colors for Better Readability
color_palette = pc.qualitative.Set2  # 🔹 Using a distinct color set

# **Scatter Plot: Budget vs Predicted Conversion Rate**
st.subheader("💡 Budget vs Predicted Conversion Rate")
fig1 = px.scatter(
    filtered_df, x="Budget", y="Rf_Predicted", size="Clicks", color="Region",
    hover_data=["CPC", "CTR"], template="plotly_white", title="Budget vs Predicted Conversion Rate",
    color_discrete_sequence=color_palette
)
st.plotly_chart(fig1, use_container_width=True)

# Compute Average Predicted Conversion Rate per Region
df_grouped = df.groupby("Region")[["Rf_Predicted", "LR_Predicted"]].mean().reset_index()

# Create Side-by-Side Bar Chart (By Region)
fig_bar = px.bar(
    df_grouped, 
    x="Region", 
    y=["Rf_Predicted", "LR_Predicted"],  # Compare both models
    barmode="group",  # Side-by-side bars
    title="Average Predicted Conversion Rates by Region (RF vs LR)",
    labels={"value": "Avg Predicted Conversion Rate", "variable": "Model"},
    color_discrete_map={"Rf_Predicted": "salmon", "LR_Predicted": "darkorange"}  # Match colors
)

#  Display in Streamlit
st.subheader(" Average Predicted Conversion Rates by Region")
st.plotly_chart(fig_bar, use_container_width=True)


#  **Bar Chart: RF vs LR Predicted Conversion Rate by Platform**
fig_bar2 = px.bar(
    filtered_df, x="Platform", y=["Rf_Predicted", "LR_Predicted"],
    title="RF vs LR Predicted Conversion Rate by Platform",
    labels={"value": "Predicted Conversion Rate", "Platform": "Platform"},
    barmode="group",
    color_discrete_map={"Rf_Predicted": "#FF6347", "LR_Predicted": "#4682B4"}  # 🔹 Red & Blue for distinction
)
st.plotly_chart(fig_bar2, use_container_width=True)

# **Simplified Box Plot: Model Prediction Error Comparison**
st.subheader("📉 Model Prediction Error")

# Ensure the columns exist before using them
if "RF_Error" not in filtered_df.columns or "LR_Error" not in filtered_df.columns:
    filtered_df["RF_Error"] = filtered_df["Actual"] - filtered_df["Rf_Predicted"]
    filtered_df["LR_Error"] = filtered_df["Actual"] - filtered_df["LR_Predicted"]

# Melt DataFrame after confirming the columns exist
error_df = filtered_df.melt(value_vars=["RF_Error", "LR_Error"], var_name="Model", value_name="Prediction Error")

#  Create Box Plot
fig_box = px.box(
    error_df,
    x="Model", y="Prediction Error", color="Model",
    title="Model Prediction Error Comparison",
    points=False,  # Hide individual points for simplicity
    boxmode="group"
)

# Improve aesthetics
fig_box.update_traces(marker=dict(opacity=0.6))  # Adjust transparency for cleaner look
fig_box.update_layout(showlegend=False, yaxis_title="Prediction Error")

st.plotly_chart(fig_box, use_container_width=True)


#  **Pie Chart: Success Rate Distribution**
fig_pie = px.pie(
    filtered_df, names="Success", title=" Success vs. Failure Distribution",
    color="Success", color_discrete_map={1: "green", 0: "red"}
)
st.plotly_chart(fig_pie, use_container_width=True)
