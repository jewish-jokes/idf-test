import pandas as pd
from sqlalchemy import create_engine
import dash_ag_grid as dag
from dash import Dash, html
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from config import USER, PASSWORD, HOST, DATABASE

engine = create_engine(f'mysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}') 

df_table = pd.read_sql("""
SELECT product_code as Product, MONTHNAME(order_date) as Month, SUM(sales_qty * sales_amount) as Sales
FROM transactions
WHERE YEAR(order_date) = "2020"
GROUP BY Product, Month
ORDER BY Product
""", engine)

df_chart = pd.read_sql("""
SELECT product_code as Product, MONTHNAME(order_date) as Month, SUM(sales_qty * sales_amount) as Sales
FROM transactions
WHERE YEAR(order_date) = "2020"
GROUP BY Product, Month
""", engine)
# Pivot the DataFrame to prepare data for the chart
pivot_df_chart = df_chart.pivot(index='Product', columns='Month', values='Sales').fillna(0)


app = Dash(__name__)

# Define a color map for months
colors = px.colors.qualitative.Set3

# Create a stacked bar chart figure
fig = px.bar(
    pivot_df_chart,
    x=pivot_df_chart.index,
    y=pivot_df_chart.columns,
    title='Total Sales by Product and Month',
    height=750,
    color_discrete_sequence=colors,
    orientation='v'
)

fig.update_xaxes(title_text='Product')  # Update x-axis label
fig.update_yaxes(title_text='Total Sales')  # Update y-axis label

# Update the layout
fig.update_layout(barmode='stack', xaxis_tickangle=-45)

# Define the app layout
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

# define table columns
columnDefs = [
    {"field": "Product"},
    {"field": "Month"},
    {"field": "Sales"},
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="row-sorting-simple",
            rowData=df_table.to_dict("records"),
            columnDefs=columnDefs,
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            columnSize="sizeToFit",
            style={'height': '750px'}
        ),
        dcc.Graph(figure=fig),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
