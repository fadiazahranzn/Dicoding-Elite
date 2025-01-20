import pandas as pd
import streamlit as st
import streamlit_shadcn_ui as ui
from charts import create_pie_chart, create_treemap, create_funnel_chart, create_plot_average_by_group

# Load the data
df = pd.read_csv('data/sleep_health.csv')

# Set the page layout to wide
st.set_page_config(layout="wide")

# Sidebar for filtering based on sleep disorders
sleep_disorder = df["sleep_disorder"].unique().tolist()
with st.sidebar:
    st.text("Total Population:")
    ui.badges(badge_list=[(f"{len(df)}", "secondary")], key="total_data")
    selected_data = st.multiselect("Select Data Based on Sleep Disorder", sleep_disorder, sleep_disorder)

# Filter the dataframe based on the selected sleep disorders
filtered_df = df[df["sleep_disorder"].isin(selected_data)]

# Create visualizations
# First row of visualizations (3 charts in a row)
first_visual = st.columns(3)
first_visual[0].plotly_chart(create_pie_chart(filtered_df, "gender", "Gender", hole=0.4))
first_visual[1].plotly_chart(create_funnel_chart(filtered_df, column="blood_pressure_category", label="Blood Pressure"))
first_visual[2].plotly_chart(create_pie_chart(filtered_df, "bmi_category", "BMI"))

# Second row of visualizations (2 charts in a row)
second_visual = st.columns(2)
second_visual[0].plotly_chart(create_treemap(filtered_df, "occupation", "Job"))
with second_visual[1]:
    st.markdown("**Filtered Data**")
    st.dataframe(filtered_df)

# Third row of visualizations (2 charts in a row)
third_visual = st.columns(2)
third_visual[0].plotly_chart(create_plot_average_by_group(filtered_df, group_column="age_group", value_column="daily_steps"))
third_visual[1].plotly_chart(create_plot_average_by_group(filtered_df, group_column="age_group", value_column="sleep_duration"))
