 # Initial Data Loading and Setup
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib as plt

# Set page configuration FIRST (to avoid Streamlit errors)
st.set_page_config(page_title="Sri Lanka Data Analysis Dashboard(Gender)", page_icon="🇱🇰", layout="wide")

# Load dataset
dataset_path = '/Users/minalsanpathfernando/Desktop/DSPL INDIVIDUAL/DSPL/gender_lka1.csv'
df = pd.read_csv(dataset_path)

# Filter Sri Lanka-only data
sri_lanka_df = df[df['Country Name'] == 'Sri Lanka']

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [" Dashboard", "Dashboard Outline"])

# Metrics and Header Display
if page == " Dashboard":
    st.title("🌍🇱🇰Sri Lanka Data Analysis Dashboard")
    st.markdown("---")
    st.markdown("This dashboard visualizes key indicators related to Sri Lanka, using interactive plots and summary statistics.")
    st.markdown("---")

    # Metric Calculations
    total_records = len(sri_lanka_df)
    total_years = sri_lanka_df['Year'].nunique()
    average_value = round(pd.to_numeric(sri_lanka_df['Value'], errors='coerce').mean(), 2)

    # Display Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", total_records)
    col2.metric("Unique Years", total_years)
    col3.metric("Average Value", average_value)

    st.markdown("---")

    # Commit 3: Raw Data Preview
    with st.expander("View Raw Data"):
        st.dataframe(sri_lanka_df)

    # ------------------------------------------
    # Commit 4: Indicator Selection and Filtering
    # ------------------------------------------
    indicator = st.selectbox("Select an Indicator to Analyze", sri_lanka_df['Indicator Name'].unique())

    filtered_data = sri_lanka_df[sri_lanka_df['Indicator Name'] == indicator]
    filtered_data['Value'] = pd.to_numeric(filtered_data['Value'], errors='coerce')

    if filtered_data['Value'].isna().sum() > 0:
        st.warning("Some non-numeric values were found and ignored in calculations.")

    df_trend = filtered_data.groupby('Year')['Value'].mean().reset_index()

    # ------------------------------------------
    # Commit 5: Tabs for Visualizations
    # ------------------------------------------
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "Line Chart", "Bar Chart", "Scatter Plot", "Box Plot", "Histogram", "Area Chart", "Statistics"
    ])

    with tab1:
        st.subheader(f"{indicator} Over the Years in Sri Lanka")
        fig_line = px.line(filtered_data, x='Year', y='Value', markers=True,
                           title=f"{indicator} Over the Years in Sri Lanka",
                           template='plotly_white')
        st.plotly_chart(fig_line, use_container_width=True)

    with tab2:
        st.subheader("Top 10 Highest Values (Bar Chart)")
        top10_df = filtered_data.sort_values(by='Value', ascending=False).head(10)
        fig_bar = px.bar(top10_df, x='Year', y='Value', color='Year',
                         title="Top 10 Highest Indicator Values",
                         template='plotly_white')
        st.plotly_chart(fig_bar, use_container_width=True)

    with tab3:
        st.subheader("Scatter Plot: Value vs Year")
        fig_scatter = px.scatter(filtered_data, x='Year', y='Value', size='Value', color='Year',
                                 title="Scatter Plot of Indicator Values",
                                 template='plotly_white')
        st.plotly_chart(fig_scatter, use_container_width=True)

    with tab4:
        st.subheader("Box Plot: Value Distribution per Year")
        fig_box = px.box(filtered_data, x='Year', y='Value', points="all",
                         title="Distribution of Indicator Values",
                         template='plotly_white')
        st.plotly_chart(fig_box, use_container_width=True)

    with tab5:
        st.subheader("Histogram: Distribution of Values")
        fig_hist = px.histogram(filtered_data, x='Value', nbins=20,
                                title="Histogram of Indicator Values",
                                template='plotly_white')
        st.plotly_chart(fig_hist, use_container_width=True)

    with tab6:
        st.subheader("Area Chart: Cumulative Trend Over Years")
        fig_area = px.area(df_trend, x='Year', y='Value',
                           title="Cumulative Indicator Trend",
                           template='plotly_white')
        st.plotly_chart(fig_area, use_container_width=True)

    with tab7:
        st.subheader("Summary Statistics")
        st.write(filtered_data[['Year', 'Value']].describe())

    # ------------------------------------------
    # Commit 6: Download CSV Section
    # ------------------------------------------
    st.markdown("---")
    st.subheader("Download Filtered Data")
    csv = filtered_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name='sri_lanka_filtered_data.csv',
        mime='text/csv',
    )

# ------------------------------------------
# Commit 7: Dashboard Outline Page
# ------------------------------------------
elif page == "Dashboard Outline":
    st.title("Dashboard Outline: Sri Lanka Data Analysis Dashboard")
    st.markdown("---")

    st.subheader("1. Title of Dashboard")
    st.markdown("> **Sri Lanka Data Analysis Dashboard**")

    st.subheader("2. Main Purpose")
    st.markdown("""
    - Provide an interactive platform to explore Sri Lankan indicators.
    - Enable dynamic visualizations for trends, comparisons, and distributions.
    - Allow data filtering by selecting specific indicators.
    - Offer the option to download filtered data easily.
    """)

    st.subheader("3. Target Users")
    st.markdown("""
    - Government Officials  
    - Data Scientists  
    - Policy Makers  
    - Academic Researchers  
    """)

    st.subheader("4. Dashboard Sections")
    st.markdown("""
    | Section Name           | Functionality                                   |
    |:------------------------|:------------------------------------------------|
    | Header Section       | Title, description, introduction to the app    |
    | Key Metrics          | Quick statistics: Total Records, Unique Years, Average Value |
    | Raw Data Preview     | View the uploaded and filtered dataset         |
    | Filter by Indicator  | Dropdown to select specific indicators         |
    | Visualization Tabs   | Line Chart, Bar Chart, Scatter, Box Plot, Histogram, Area Chart |
    | Download Section     | Export filtered data as CSV                    |
    """, unsafe_allow_html=True)

    st.subheader("5. Technologies Used")
    st.markdown("""
    - Python (Pandas, Streamlit, Plotly)  
    - Streamlit Cloud (for deployment)  
    - GitHub (for version control)  
    - VS Code (for development)  
    """)

    st.subheader("6. Visualizations Provided")
    st.markdown("""
    - Line Chart — Trends over Years  
    - Bar Chart — Top 10 Values  
    - Scatter Plot — Spread across Years  
    - Box Plot — Distribution Analysis  
    - Histogram — Value Frequency  
    - Area Chart — Cumulative Trends  
    - Statistics — Summary Table  
    """)

    st.subheader("7. Final Features Summary")
    st.markdown("""
    - Interactive and Dynamic Interface  
    - Fast Data Filtering  
    - Clean and Professional Visuals  
    - CSV Export Option  
    - Responsive Layout  
    """)
