# charts.py
import plotly.express as px
import plotly.graph_objects as go

def create_pie_chart(df, column, title, hole=0):
    fig = px.pie(df, names=column, title=title)
    fig.update_traces(hole=hole, hoverinfo="label+percent+name")
    return fig

def create_funnel_chart(df, column, label):
    # Assuming the column is categorical and sorted in a funnel-like manner
    fig = go.Figure(go.Funnel(
        y=df[column].value_counts().index,
        x=df[column].value_counts().values
    ))
    fig.update_layout(title=f"{label} Funnel Chart")
    return fig

def create_treemap(df, column, title):
    fig = px.treemap(df, path=[column], title=title)
    return fig

def create_plot_average_by_group(df, group_column, value_column):
    avg_values = df.groupby(group_column)[value_column].mean().reset_index()
    fig = px.bar(avg_values, x=group_column, y=value_column, title=f"Average {value_column} by {group_column}")
    return fig
