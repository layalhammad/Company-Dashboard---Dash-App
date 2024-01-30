import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import dcc, html, callback, register_page
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


dash.register_page(__name__, path ='/')

# Load Data
# Sales df
# Product lines df
# Customers df
#forecast df 
# target Sales df

# ----------------------------------------------------------------------------

#clean dataframes

# ----------------------------------------------------------------------------

# merge datasets: sales, customers, itemcat

# ----------------------------------------------------------------------------

# years for Dropdown
years = mergedf.year.unique()
years.sort()

# ----------------------------------------------------------------------------


#APP Page 1: Company's Sales

import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

slider = html.Div(
    [
        html.Label("Select Year", htmlFor="years"),
        dcc.Slider(
            min=years[0],
            max=years[-1],
            step=1,
            value=years[-1],
            id="years",
            marks={i: f'{i}' for i in years.astype(str)},
            tooltip={"placement": "top", "always_visible": True},
        ),
    ]
)

dropdownsales = html.Div([
    dcc.Dropdown(
        options=mergedf['SalesmanName'].unique(),
        placeholder="Select a Sales Person",
        clearable=True,
        id='salesman')])

# Build App

# # Create Dash app
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

layout = html.Div(

    [dbc.Row([
              dbc.Col([html.H1("Company's Sales", style={'color': '#5E5C5C', 'text-align': 'center', 'font-size': '72px', \
                                                   'backgroundColor': 'White'})])
              ]),
     dbc.Row(style={ "height": "2vh"}),
     dbc.Row(
         [dbc.Col([dcc.Graph(id='TotSales')]), dbc.Col([dcc.Graph(id='PerSales')]), dbc.Col([dcc.Graph(id='Gross')])]),
     dbc.Row(style={"height": "5vh"}),
     dbc.Row([dbc.Col(dropdownsales), dbc.Col(slider)]),
     dbc.Row([dbc.Col([dcc.Graph(id='Sales')]), dbc.Col([dcc.Graph(id='Per')])]),
     dbc.Row([dbc.Col([dcc.Graph(id='radar')]), dbc.Col([dcc.Graph(id='forecastvsreality')])]),
     dbc.Row([dbc.Col([dcc.Graph(id='Sector')]), dbc.Col([dcc.Graph(id='TOP')])])
     ]
)

colors = {'Armstrong': '#FDFDBD', 'Shroder': '#F4BFBF', 'Mortara': "#eac4d5", 'Tecme': '#B8E8FC', \
          "Welch Allyn": '#B1AFFF', 'Stihler': ' #ffc09f', 'Ceracarta': '#a0ced9', \
          'KERN': '#b8e0d2', 'CONTE': '#d6eadf', 'MEYSA': '#e8d1c5', '999': '#95b8d1', \
          'LOCAL': '#adf7b6', 'BIO': '#ff615d', 'PM': '#bad5ea', 'MAI': '#fd8769', 'Ion': '#356d94', \
          'Pacific': '#ffdcb3', 'NEAR': '#4f3268', 'Hill Rom': '#9d78be', 'Track Master': '#e3a9c1', \
          'B.A.I': '#f3e3ed', 'ENDOD': '#aaaaaa', 'KEJIA': '#2ea1da', 'BISTO': '#e83879'}


# Call back to update salesman options
@callback(
    Output('salesman', "options"),
    [Input("years", "value")])
def sales_options(selected_year):
    filtered_df = mergedf[mergedf['year'] == selected_year]
    return [{"label": i, "value": i} for i in filtered_df['SalesmanName'].unique()]


# Define callback to update sales indicator
@callback(
    Output('TotSales', 'figure'),
    [Input("years", "value"),
     Input('salesman', 'value')]
)
def update_indicator_sales(selected_year, salesman):
    filtered_dff = mergedf[mergedf['year'] == selected_year]
    filtered_dff2 = filtered_dff[filtered_dff['SalesmanName'] == salesman]

    target_year = target[target['Year'] == selected_year]
    target_sp = target_year[target_year['Employee Name'] == salesman]

    # for no salesmen
    totalSales = go.Figure(go.Indicator(
        mode="number+delta",
        value=filtered_dff.Sell.sum(),
        number={'suffix': " USD", "font": {"size": 25}},
        delta={'position': "top", 'reference': target_year.sum()['Annual Target'], "font": {"size": 20}},
        title={"text": "Sales", "font": {"size": 30}},
        domain={'x': [0, 1], 'y': [0, 1]}))

    totalSales.update_layout(paper_bgcolor="#F4F4F4", height=200)

    totalSales2 = go.Figure(go.Indicator(
        mode="number+delta",
        value=filtered_dff2.Sell.sum(),
        number={'suffix': " USD", "font": {"size": 25}},
        delta={'position': "top", 'reference': target_sp.sum()['Annual Target'], "font": {"size": 20}},
        title={"text": "Sales", "font": {"size": 30}},
        domain={'x': [0, 1], 'y': [0, 1]}))

    totalSales2.update_layout(paper_bgcolor="#F4F4F4", height=200)

    # for updated salesmen

    if salesman is None:
        return totalSales
    else:
        return totalSales2

    # Define callback to update sales percentage indicator


@callback(
    Output('PerSales', 'figure'),
    [Input("years", "value"),
     Input('salesman', 'value')]
)
def update_indicator_sales(selected_year, salesman):
    filtered_dff = mergedf[mergedf['year'] == selected_year]
    filtered_dff2 = filtered_dff[filtered_dff['SalesmanName'] == salesman]

    target_year = target[target['Year'] == selected_year]
    target_sp = target_year[target_year['Employee Name'] == salesman]

    # for no salesmen
    perSales = go.Figure(go.Indicator(
        mode="number+delta",
        value=(filtered_dff.Sell.sum() / target_year.sum()['Annual Target']) * 100,
        number={'suffix': " %", "font": {"size": 25}},
        delta={'position': "top", 'reference': 100, "font": {"size": 20}},
        title={"text": "Sales Achievement", "font": {"size": 30}},
        domain={'x': [0, 1], 'y': [0, 1]}))

    perSales.update_layout(paper_bgcolor="#F4F4F4", height=200)

    perSales2 = go.Figure(go.Indicator(
        mode="number+delta",
        value=(filtered_dff2.Sell.sum() / target_sp.sum()['Annual Target']) * 100,
        number={'suffix': " %", "font": {"size": 25}},
        delta={'position': "top", 'reference': 100, "font": {"size": 20}},
        title={"text": "Sales Achievement", "font": {"size": 30}},
        domain={'x': [0, 1], 'y': [0, 1]}))

    perSales2.update_layout(paper_bgcolor="#F4F4F4", height=200)

    # for updated salesmen

    if salesman is None:
        return perSales
    else:
        return perSales2

    # Define callback to update Gross indicator


@callback(
    Output('Gross', 'figure'),
    [Input("years", "value"),
     Input('salesman', 'value')]
)
def update_indicator_gross(selected_year, salesman):
    filtered_dff = mergedf[mergedf['year'] == selected_year]
    filtered_dff2 = filtered_dff[filtered_dff['SalesmanName'] == salesman]

    target_year = target[target['Year'] == selected_year]
    target_sp = target_year[target_year['Employee Name'] == salesman]

    # for no salesmen
    gross = go.Figure(go.Indicator(
        mode="number+delta",
        value=round((filtered_dff.Sell.sum() - filtered_dff.Cost.sum()) / filtered_dff.Sell.sum() * 100, 2),
        number={'suffix': " %", "font": {"size": 25}},
        delta={'position': "top", 'reference': target_year['Targeted Gross Margin'].mean() * 100, "font": {"size": 20}},
        title={"text": "Gross Margin", "font": {"size": 30}},
        domain={'x': [0, 1], 'y': [0, 1]}))

    gross.update_layout(paper_bgcolor="#F4F4F4", height=200)

    gross2 = go.Figure(go.Indicator(
        mode="number+delta",
        value=round((filtered_dff2.Sell.sum() - filtered_dff2.Cost.sum()) / filtered_dff2.Sell.sum() * 100, 2),
        number={'suffix': " %", "font": {"size": 25}},
        delta={'position': "top", 'reference': target_sp['Targeted Gross Margin'].mean() * 100, "font": {"size": 20}},
        title={"text": "Gross Margin", "font": {"size": 30}},
        domain={'x': [0, 1], 'y': [0, 1]}))

    gross2.update_layout(paper_bgcolor="#F4F4F4", height=200)

    # for updated salesmen

    if salesman is None:
        return gross
    else:
        return gross2

#         # Define callback to update Hospital indicator


# @app.callback(
#     Output('Hosp', 'figure'),
#     [Input("years", "value"),
#      Input('salesman', 'value')]
# )
# def update_indicator_hosp(selected_year, salesman):
#     filtered_dff = mergedf[mergedf['year'] == selected_year]
#     filtered_dff2 = filtered_dff[filtered_dff['SalesmanName'] == salesman]

#     target_year = target[target['Year'] == selected_year]
#     target_sp = target_year[target_year['Employee Name'] == salesman]

#     # for no salesmen
#     gross = go.Figure(go.Indicator(
#         mode="number+delta",
#         value=round((filtered_dff.Sell.sum() - filtered_dff.Cost.sum()) / filtered_dff.Sell.sum() * 100, 2),
#         number={'suffix': " %", "font": {"size": 25}},
#         delta={'position': "top", 'reference': target_year['Targeted Gross Margin'].mean() * 100, "font": {"size": 20}},
#         title={"text": "Gross Margin", "font": {"size": 30}},
#         domain={'x': [0, 1], 'y': [0, 1]}))

#     gross.update_layout(paper_bgcolor="lightgray", height=200)

#     gross2 = go.Figure(go.Indicator(
#         mode="number+delta",
#         value=round((filtered_dff2.Sell.sum() - filtered_dff2.Cost.sum()) / filtered_dff2.Sell.sum() * 100, 2),
#         number={'suffix': " %", "font": {"size": 25}},
#         delta={'position': "top", 'reference': target_sp['Targeted Gross Margin'].mean() * 100, "font": {"size": 20}},
#         title={"text": "Gross Margin", "font": {"size": 30}},
#         domain={'x': [0, 1], 'y': [0, 1]}))

#     gross2.update_layout(paper_bgcolor="lightgray", height=200)

#     # for updated salesmen

#     if salesman is None:
#         return gross
#     else:
#         return gross2

    # Define callback to update graph


@callback(
    Output('Sales', 'figure'),
    [Input("years", "value"),
     Input('salesman', 'value')]
)
def update_graph_a(selected_year, salesman):
    filtered_df = mergedf[mergedf['year'] == selected_year]
    filtered_df2 = filtered_df[filtered_df['SalesmanName'] == salesman]

    # for no salesmen
    line_fig = px.bar(filtered_df.groupby(['brand', 'Category'])['Sell'].sum().reset_index(), y="Category", x="Sell",
                      color="brand", \
                      color_discrete_map=colors, orientation='h')

    line_fig.update_layout(plot_bgcolor='white',
                           title_text=f'Company's Sales in {selected_year}', title_x=0.5, xaxis_title='Manufacturer',
                           yaxis_title='Sales')

    # for updated salesmen
    line_fig2 = px.bar(filtered_df2.groupby(['brand', 'Category'])['Sell'].sum().reset_index(), y="Category", x="Sell",
                       color="brand", \
                       color_discrete_map=colors, orientation='h')

    line_fig2.update_layout(plot_bgcolor='white',
                            title_text=f'Company's Sales in {selected_year}', title_x=0.5, xaxis_title='Manufacturer',
                            yaxis_title='Sales')

    #     line_fig.update_layout(legend=dict(y=1,x=-1.2))

    if salesman is None:
        return line_fig
    else:
        return line_fig2


# Define callback to update graph b
@callback(
    Output('Per', 'figure'),
    [Input("years", "value"),
     Input('salesman', 'value')]
)
def update_graph_b(selected_year, salesman):
    filtered_dff = mergedf[mergedf['year'] == selected_year]
    filtered_dff2 = filtered_dff[filtered_dff['SalesmanName'] == salesman]

    # for no salesmen
    brandper = go.Figure(data=[go.Pie(labels=filtered_dff['brand'], values=filtered_dff['Sell'], hole=.6)])
    brandper.update_traces(marker=dict(colors=filtered_dff["brand"].map(colors), line=dict(color='#FFFFFF', width=3)))
    brandper.update_layout(showlegend=False, title_text='Brand Share', title_x=0.5)

    ## for updated salesmen
    brandper2 = go.Figure(data=[go.Pie(labels=filtered_dff2['brand'], values=filtered_dff2['Sell'], hole=.6)])
    brandper2.update_traces(marker=dict(colors=filtered_dff2["brand"].map(colors), line=dict(color='#FFFFFF', width=3)))
    brandper2.update_layout(showlegend=False, title_text='Brand Share', title_x=0.5)

    if salesman is None:
        return brandper
    else:
        return brandper2

    # Define callback to update graph c


@callback(
    Output('radar', 'figure'),
    [Input("years", "value"),
     Input('salesman', 'value')]
)
def update_graph_c(selected_year, salesman):
    filtered_dff = mergedf[mergedf['year'] == selected_year]
    filtered_dff2 = filtered_dff[filtered_dff['SalesmanName'] == salesman]

    # for no salesmen
    test = filtered_dff.groupby('Category')['Sell'].sum().sort_values(ascending=False).reset_index()
    test['per'] = test['Sell'].transform(lambda x: 100 * x / x.sum())
    numb = test["Sell"]
    radar_fig = go.Figure(data=go.Scatterpolar(
        r=test['per'].head(8),
        theta=test['Category'].head(8),
        fill='toself',
        customdata=test['Sell'].head(8),
        hovertemplate='Product Line: <b>%{theta}</b><br>' + 'Sales: <b>%{customdata}</b><br>'
                      + 'Sales Percentage: <b>%{r}</b><br>'
    ))

    radar_fig.update_layout(
        polar=dict(bgcolor='white', angularaxis_gridcolor='#ededed', angularaxis_linecolor='#ededed',

                   radialaxis=dict(
                       visible=True),
                   ),
        showlegend=False)
    radar_fig.update_layout(title_text='Spread', \
                            title_x=0.5)

    # for updated salesmen
    test2 = filtered_dff2.groupby('Category')['Sell'].sum().sort_values(ascending=False).reset_index()
    test2['per'] = test2['Sell'].transform(lambda x: 100 * x / x.sum())
    radar_fig2 = go.Figure(data=go.Scatterpolar(
        r=test2['per'].head(8),
        theta=test2['Category'].head(8),
        fill='toself',
        customdata=test2['Sell'].head(8),
        hovertemplate='Product Line: <b>%{theta}</b><br>' + 'Sales: <b>%{customdata}</b><br>'
                      + 'Sales Percentage: <b>%{r}</b><br>'

    ))

    radar_fig2.update_layout(
        polar=dict(bgcolor='white', angularaxis_gridcolor='#ededed', angularaxis_linecolor='#ededed',

                   radialaxis=dict(
                       visible=True),
                   ),
        showlegend=False)
    radar_fig2.update_layout(title_text='Spread', \
                             title_x=0.5)

    if salesman is None:
        return radar_fig
    else:
        return radar_fig2

    # Define callback to update graph d


@callback(
    Output('forecastvsreality', 'figure'),
    [Input("years", "value"),
     Input('salesman', 'value')]
)
def update_graph_d(selected_year, salesman):
    # Actual Sales
    filtered_dff = mergedf[mergedf['year'] == selected_year]
    filtered_dff2 = filtered_dff[filtered_dff['SalesmanName'] == salesman]

    # Forecast - Removing less than 50% probability
    forecast_fdf = forecastdf.drop(
        forecastdf[forecastdf.Probability.isin(['1% (Opportunity Identified)', '0% (lost)', '0% (cancelled)', '25% (Active)', '30% (Offer submitted - low chance)'])].index)

    # Forecast
    forecast_fdff = forecast_fdf[forecast_fdf['Fiscal Year'] == selected_year]
    forecast_fdff2 = forecast_fdff[forecast_fdff['Sales Person'] == salesman]

    # previous year actual sales
    filtered_dffpr = mergedf[mergedf['year'] == selected_year-1]
    filtered_dffpr2 = filtered_dffpr[filtered_dffpr['SalesmanName'] == salesman]
    
    
    # for no salesmen
    figsalesq = go.Figure(data=[
        go.Scatter(x=filtered_dff.groupby('Quarter')['Sell'].sum().reset_index()['Quarter'].astype(str),
                   y=filtered_dff.groupby('Quarter')['Sell'].sum().reset_index()['Sell'], mode='lines+markers',
                   marker_color=('#FFC7B6'), name=f'{selected_year} Actual Sales'),
        
        go.Scatter(x=filtered_dffpr.groupby('Quarter')['Sell'].sum().reset_index()['Quarter'].astype(str),
                   y=filtered_dffpr.groupby('Quarter')['Sell'].sum().reset_index()['Sell'], mode='lines+markers',
                   marker_color=('#adf7b6'), name=f'{selected_year-1} Actual Sales'),
        
        go.Scatter(
            x=forecast_fdff.groupby('Quarter')['Company's Total Price (USD)'].sum().reset_index()['Quarter'].astype(int).astype(str),
            y=forecast_fdff.groupby('Quarter')['Company's Total Price (USD)'].sum().reset_index()['Company's Total Price (USD)'],
            mode='lines+markers', \
            marker_color=('#B1AFFF'), name=f'{selected_year} Sales Forecast')])
    figsalesq.update_layout(plot_bgcolor='white', title_text='Sales Per Quarter', \
                            title_x=0.5, xaxis_title="Quarter", yaxis_title="Sales", legend=dict(x=1.0, y=0.5))
    figsalesq.update_yaxes(showgrid=True, gridwidth=0.3, gridcolor='#ededed')
    #     figsalesq.update_xaxes(showgrid=True, gridwidth=0.3, gridcolor='#ededed')

    ## for updated salesmen
    figsalesq2 = go.Figure(data=[
        go.Scatter(x=filtered_dff2.groupby('Quarter')['Sell'].sum().reset_index()['Quarter'].astype(str),
                   y=filtered_dff2.groupby('Quarter')['Sell'].sum().reset_index()['Sell'], mode='lines+markers',
                   marker_color=('#FFC7B6'), name='Actual Sales'),
        
        go.Scatter(x=filtered_dffpr2.groupby('Quarter')['Sell'].sum().reset_index()['Quarter'].astype(str),
                   y=filtered_dffpr2.groupby('Quarter')['Sell'].sum().reset_index()['Sell'], mode='lines+markers',
                   marker_color=('#adf7b6'), name=f'{selected_year-1} Actual Sales'),
        
        go.Scatter(
            x=forecast_fdff2.groupby('Quarter')['Company's Total Price (USD)'].sum().reset_index()['Quarter'].astype(int).astype(str),
            y=forecast_fdff2.groupby('Quarter')['Company's Total Price (USD)'].sum().reset_index()['Company's Total Price (USD)'],
            mode='lines+markers', \
            marker_color=('#B1AFFF'), name='Sales Forecast')])
    figsalesq2.update_layout(plot_bgcolor='white', title_text='Sales Per Quarter', \
                             title_x=0.5, xaxis_title="Quarter", yaxis_title="Sales", legend=dict(x=1.0, y=0.5))
    figsalesq2.update_yaxes(showgrid=True, gridwidth=0.3, gridcolor='#ededed')
    #     figsalesq2.update_xaxes(showgrid=True, gridwidth=0.3, gridcolor='#ededed')

    if salesman is None:
        return figsalesq
    else:
        return figsalesq2


# Define callback to update graph e
@callback(
    Output('Sector', 'figure'),
    [Input("years", "value"),
     Input('salesman', 'value')]
)
def update_graph_e(selected_year, salesman):
    filtered_dff = mergedf[mergedf['year'] == selected_year]
    filtered_dff2 = filtered_dff[filtered_dff['SalesmanName'] == salesman]

    # for no salesmen
    sector = go.Figure(data=[go.Pie(labels=filtered_dff['Private/ Public '], values=filtered_dff['Sell'], hole=.6)])
    sector.update_traces(marker=dict(colors=['rgb(251,180,174)', \
                                             'rgb(179,205,227)', 'rgb(204,235,197)', 'rgb(222,203,228)',
                                             'rgb(254,217,166)', 'rgb(255,255,204)'],
                                     line=dict(color='#FFFFFF', width=3)))
    sector.update_layout(showlegend=True, title_text=' Sector', title_x=0.5)

    ## for updated salesmen
    sector2 = go.Figure(data=[go.Pie(labels=filtered_dff2['Private/ Public '], values=filtered_dff2['Sell'], hole=.6)])
    sector2.update_traces(marker=dict(colors=['rgb(251,180,174)', \
                                              'rgb(179,205,227)', 'rgb(204,235,197)', 'rgb(222,203,228)',
                                              'rgb(254,217,166)', 'rgb(255,255,204)'],
                                      line=dict(color='#FFFFFF', width=3)))
    sector2.update_layout(showlegend=True, title_text=' Sector', title_x=0.5)

    if salesman is None:
        return sector
    else:
        return sector2

        # Define callback to update graph Top 5


@callback(
    Output('TOP', 'figure'),
    [Input("years", "value"),
     Input('salesman', 'value')]
)
def update_graph_top(selected_year, salesman):
    filtered_df = mergedf[mergedf['year'] == selected_year]
    filtered_df2 = filtered_df[filtered_df['SalesmanName'] == salesman]

    # for no salesmen
    top_fig = px.bar(filtered_df.groupby(['Name'])['Sell'].sum().sort_values(ascending=False).reset_index().head(5),
                     y="Name", x="Sell", color="Name", \
                     color_discrete_sequence=px.colors.qualitative.Pastel1, orientation='h')

    top_fig.update_layout(plot_bgcolor='white', yaxis_visible=False,
                          legend=dict(y=.5, x=0.7, title="Hospital", itemsizing='trace'),
                          title_text=f'Company's Sales in {selected_year}', title_x=0.1, xaxis_title='Top 5 Customers',
                          yaxis_title='Sales')

    # for updated salesmen
    top_fig2 = px.bar(filtered_df2.groupby(['Name'])['Sell'].sum().sort_values(ascending=False).reset_index().head(5),
                      y="Name", x="Sell", color="Name", \
                      color_discrete_sequence=px.colors.qualitative.Pastel1, orientation='h')

    top_fig2.update_layout(plot_bgcolor='white', yaxis_visible=False,
                           legend=dict(y=.5, x=0.7, title="Hospital", itemsizing='trace'),
                           title_text=f'Company's Sales in {selected_year}', title_x=0.1, xaxis_title='Top 5 Customers',
                           yaxis_title='Sales')

    if salesman is None:
        return top_fig
    else:
        return top_fig2


# # Run app externally
# if __name__ == '__main__':
#     app.run_server(debug=True, port=8050)



















