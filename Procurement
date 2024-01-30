import dash
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dash import dcc, html, callback, register_page
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

dash.register_page(__name__, path = '/purchases')

from dash import dcc, html, callback


# Load Data
# purchases df 
# product lines df
# forecast df 
# hospitals df
# market share df
# positioning df


#--------------------------------------------------------

#clean dataframes

# merge datasets


#--------------------------------------------------------


#APP Page 2: Company's Purchases


import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go




low = overall['Total Invoiced Amount ($)'].tolist()
exp = overall['Sales Forecast ($)'].tolist()
high = np.array(overall['Total Invoiced Amount ($)'])+1 # artificially added 20 to get the second graph above the first one


trace1 = go.Scatter(x=overall.Year[:1],
                    y=low[:2],
                    mode='lines',
                    marker_color=('#9DA4DB'),

                    text=round(overall['sales growth'],2),
                     name = 'Sales',
                     hovertemplate = "<b>Year: <b>%{x} <br>Sales: <b>%{y} <br>Sales Growth: <b>%{text}"
#                     line=dict(width=1.5)
                   )

trace2 = go.Scatter(x=overall.Year[:1],
                    y=exp[:2],
                    mode='lines',
                    marker_color=('#F4BFBF'),

                    text=round(overall['Sale achievement'],2),
                    name = 'Forecast',
                    hovertemplate = "<b>Year: <b>%{x} <br>Sales Achievement: <b>%{text} "
# #                     line=dict(width=1.5)
                   )



frames = [dict(data= [dict(type='scatter',
                           x=overall.Year[:k+1],
                           y=low[:k+1]),
                      dict(type='scatter',
                           x=overall.Year[:k+1],
                           y=exp[:k+1])
            
                     ],
               traces= [0, 1],  #this means that  frames[k]['data'][0]  updates trace1, and   frames[k]['data'][1], trace2 
              )for k  in  range(1, len(low))] 

layout_1 = go.Layout(width=650,
                   height=400,
                   showlegend=False,
                   hovermode='closest',
                   updatemenus=[dict(type='buttons', showactive=False,
                                y=1.05,
                                x=1.15,
                                xanchor='right',
                                yanchor='top',
                                pad=dict(t=0, r=10),
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, 
                                                    dict(frame=dict(duration=200, 
                                                                    redraw=False),
                                                         transition=dict(duration=0),
                                                         fromcurrent=True,
                                                         mode='immediate')])])])


layout_1.update(xaxis =dict(range=[overall.Year.min() - 1, overall.Year.max() + 1], autorange=False),
              yaxis =dict(range=[0, 700000], autorange=False));
figsales = go.Figure(data=[trace1,trace2], frames=frames, layout=layout_1)
figsales.update_layout( plot_bgcolor='rgba(0,0,0,0)', title_text= 'Brand Purchases Over Years', title_x=0.5, legend=dict(x=1.0, y=1.1))
figsales.update_yaxes(showgrid=True, gridwidth=0.3, gridcolor='#ededed')
figsales.update_xaxes(showgrid=True, gridwidth=0.3, gridcolor='#ededed')
figsales.update_yaxes(title_text="Sales")
figsales.update_xaxes(title_text="Year", tickvals = overall['Year'])






# -----------------------------------




slider = html.Div(
    [
        html.Label("Select Year", htmlFor="years"),
        dcc.Slider(
            min=years[0],
            max=years[-1],
            step=1,
            value=years[-1],
            id="years",
            marks= {i: f'{i}' for i in years.astype(str)},
            tooltip={"placement": "top", "always_visible": True}
        ),
    ]
)


dropdownline =  html.Div([
        dcc.Dropdown(
            options=dff['Category'].unique(),
            placeholder="Select a Product Line",
            clearable=True,
            id='Category')])

dropdownqquarter =  html.Div([
        dcc.Dropdown(
            options=sorted(dff['Quarter'].unique()),
            placeholder="Select a Quarter",
            clearable=True,
            id='Quarter')])

dropdownP =  html.Div([
        dcc.Dropdown(
            options=mer['Product Line'].unique(),
            placeholder="Select a Product",
            clearable=True,
            value='Thermometry',
            id='Product')])


# Build App


# Create Dash app
# app = JupyterDash(__name__,  external_stylesheets= [dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP] )


layout = html.Div(
    
    [
    
    dbc.Row([dbc.Col([html.H1("Company's-Brand Purchases", style = {'color':'#5E5C5C', 'text-align' : 'center', 'font-size' : '72px',"font-weight": "500",\
    'backgroundColor':'white'})])]),
    dbc.Row( style={"height": "2vh"}),                             
    dbc.Row([ dbc.Col(slider),dbc.Col(dropdownline),dbc.Col(dropdownqquarter)]),
    dbc.Row([dbc.Col([dcc.Graph(id ='totalp')]), dbc.Col([dcc.Graph(id ='pending')]), dbc.Col([dcc.Graph(id ='totalAch')]),dbc.Col([dcc.Graph(id='growth')])]),
    dbc.Row([dbc.Col([dcc.Graph(figure=figsales)],width=6),dbc.Col([dcc.Graph(id='Purchases')],width=6)]),
    dbc.Row([dbc.Col([dcc.Graph(id='P_S')])]),
    dbc.Row([dbc.Col([html.H1("Market Data", style = {'color':'white', 'text-align' : 'center', 'font-size' : '72px',\
    'backgroundColor':'grey'})])]),
    dbc.Row([ dbc.Col([dcc.Graph(id ='totalms')]),dbc.Col([dcc.Graph(id='Sectors')],width=6)]) ,
    dbc.Row([dbc.Col([html.H1("Market Share", style = {'color':'white', 'text-align' : 'center', 'font-size' : '72px',\
    'backgroundColor':'grey'})])]),
    dbc.Row([dbc.Col([dropdownP],width=2), dbc.Col([dcc.Graph(id='MS')],width=5),dbc.Col([dcc.Graph(id='Pos')],width=5)]),
    dbc.Row([dbc.Col([html.H1("Forecast", style = {'color':'white', 'text-align' : 'center', 'font-size' : '72px',\
    'backgroundColor':'grey'})])]),
    dbc.Row([ dbc.Col([dcc.Graph(id='forecastpl')], width=6),dbc.Col([dcc.Graph(id='forecast')],width=6)]) 
    ]
)



# Define callback to update purchases indicator
@callback(
    Output('totalp', 'figure'),
    [Input("years", "value")]
)


def update_indicator_totalp(selected_year):

    filtered_dff = overall[overall['Year'] == selected_year]
    
    
    totalp = go.Figure(go.Indicator(
    mode = "number+delta",
    value = filtered_dff['Total Invoiced Amount ($)'].mean(),
    number = {'prefix': "$ ", "font":{"size":25}},
    delta = {'position': "top", 'reference':filtered_dff['Sales Forecast ($)'].mean(), "font":{"size":20}},
    title = {"text": "Total Purchases", "font":{"size":30}},
    domain = {'x': [0, 1], 'y': [0, 1]}))

    totalp.update_layout(paper_bgcolor = "#F4F4F4",height=200)
    

    return totalp



# Define callback to update purchases indicator
@callback(
    Output('pending', 'figure'),
    [Input("years", "value")]
)


def update_indicator_pending(selected_year):

    filtered_dff = pend[pend['Year'] == selected_year]
    
    
    pending = go.Figure(go.Indicator(
    mode = "number+delta",
    value = filtered_dff['Pending Orders'].mean(),
    number = {'prefix': "$ ", "font":{"size":25}},
    delta = {'position': "top",  "font":{"size":20}},
    title = {"text": "Pending Orders", "font":{"size":30}},
    domain = {'x': [0, 1], 'y': [0, 1]}))

    pending.update_layout(paper_bgcolor = "#F4F4F4",height=200)
    

    return pending





# Define callback to update Target Achievement indicator
@callback(
    Output('totalAch', 'figure'),
    [Input("years", "value")]
)


def update_indicator_totalAch(selected_year):

    filtered_dff = overall[overall['Year'] == selected_year]
    
    
    totalAch = go.Figure(go.Indicator(
    mode = "number+delta",
    value = filtered_dff['Sale achievement'].mean(),
    number = {'suffix': " %", "font":{"size":25}},
    delta = {'position': "top", 'reference':100, "font":{"size":20}},
    title = {"text": "Target Achievement", "font":{"size":30}},
    domain = {'x': [0, 1], 'y': [0, 1]}))

    totalAch.update_layout(paper_bgcolor = "#F4F4F4",height=200)
    

    return totalAch    



# Define callback to update Achievement indicator
@callback(
    Output('growth', 'figure'),
    [Input("years", "value")]
)


def update_indicator_growth(selected_year):

    filtered_dff = overall[overall['Year'] == selected_year]
    
    
    totalg = go.Figure(go.Indicator(
    mode = "number+delta",
    value = filtered_dff['sales growth'].mean(),
    number = {'suffix': " %",'font_color':'#F4F4F4', 'font_size':25},
    delta = {'suffix': " %", 'position': "bottom",  'reference':0.0001, "font":{"size":25}},
    title = {"text": "Growth", "font":{"size":30}},
    domain = {'x': [0, 1], 'y': [0, 1]}))

    totalg.update_layout(paper_bgcolor = "#F4F4F4",height=200)
    

    return totalg

##########

@callback(
    Output('totalms', 'figure'),
    [Input("years", "value")]
)

def update_indicator_yearlyms(selected_year):

    filtered_dfff = overallfor[overallfor['Fiscal Year'] == selected_year]
    filtered_dff = overall[overall['Year'] == selected_year]
    
    totalms = go.Figure(go.Indicator(
    mode = "number+delta",
    value = filtered_dff['Total Invoiced Amount ($)'].mean()/filtered_dfff['Manufacturer Total Value USD'].mean()*100,
    number = {'suffix': " %",  "font":{"size":25}},
    delta = {'position': "top", "font":{"size":25}},
    title = {"text": f"Market Share in {selected_year}", "font":{"size":30}},
    domain = {'x': [0, 1], 'y': [0, 1]}))

    totalms.update_layout(paper_bgcolor = "#F4F4F4",height=200)
    

    return totalms





# Define callback to update graph sector share
@callback(
    Output('Sectors', 'figure'),
    [Input("years", "value")]
)
def update_graph_e(selected_year):
    filtered_dff = per

    sector = go.Figure(data=[go.Pie(labels=filtered_dff[['Sector']], values=filtered_dff['percent'], hole=.6, customdata=filtered_dff['beds'])])
    sector.update_traces(hovertemplate = "Sector: %{label} <br>Beds: %{customdata}", marker=dict(colors=['rgb(251,180,174)', \
                                             'rgb(179,205,227)', 'rgb(204,235,197)', 'rgb(222,203,228)',
                                             'rgb(254,217,166)', 'rgb(255,255,204)'],
                                     line=dict(color='#FFFFFF', width=3)))
    sector.update_layout(showlegend=True, title_text='Healthcare Sector', title_x=0.5)

    return sector






# Define callback to update graph
@callback(
    Output('Purchases', 'figure'),
    [Input("years", "value")],
    [Input("Quarter", "value")]
)

def update_graph(selected_year, Quarter):
    filtered_df = dff[(dff['Year'] == selected_year) | (dff['Year'] == selected_year - 1)]
    filtered_dff = dff[dff['Year'] == selected_year]
    filtered_df2 = filtered_dff[filtered_dff['Quarter']== Quarter]

    #for no quarter
    line_fig = px.histogram(filtered_df, y="Category", x="Total Invoiced Amount ($)",orientation='h', color = 'Year',color_discrete_sequence=px.colors.qualitative.Pastel1, text_auto='.2s')
    line_fig.update_layout(barmode='overlay',plot_bgcolor='white',
            title_text= f'Company's Purchases in {selected_year}', title_x=0.5, xaxis_title = 'Amount',yaxis_title='Product Line')
    line_fig.update_xaxes(dtick=50000)
    line_fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
   

    #for specific quarter
    line_fig2 = px.bar(filtered_df2, y="Category", x="Total Invoiced Amount ($)",orientation='h', color = 'Supplier Name',color_discrete_sequence=px.colors.qualitative.Pastel1)
    line_fig2.update_layout(plot_bgcolor='white',
            title_text= f'Company's Purchases in Q{Quarter}', title_x=0.5, xaxis_title = 'Amount',yaxis_title='Product Line')

    if Quarter is None:
        return line_fig
    else:
        return line_fig2 



# # Define callback to update graph
@callback(
    Output('P_S', 'figure'),
    [Input("years", "value")],
    [Input("Category", "value")]
 )

def update_graph_b(selected_year,Category):
    filtered_df = com[com['year'] == selected_year]
    filtered_df2 = filtered_df[filtered_df['Product Line']== Category]
    
#   for no product line
    sp_fig = px.bar(filtered_df, y=["P_QTY","S_QTY"], x='Product ID',   color_discrete_sequence=px.colors.qualitative.Pastel1)
    sp_fig.update_layout(plot_bgcolor='white',barmode='group',
            title_text= f'Company's Purchases vs Sales in {selected_year}', title_x=0.5, xaxis_title = 'Product ID',yaxis_title='Quantity')
    sp_fig.update_xaxes(type='category')

    
#   for specific product line
    sp_fig2 = px.bar(filtered_df2, y=["P_QTY","S_QTY"], x='Product ID', color_discrete_sequence=px.colors.qualitative.Pastel1)
    sp_fig2.update_layout(plot_bgcolor='white',barmode='group',
            title_text= f'Company's Purchases vs Sales in {selected_year}', title_x=0.5, xaxis_title = 'Product ID',yaxis_title='Quantity')
    sp_fig2.update_xaxes(type='category') 
    
    if Category is None:
        return sp_fig
    else:
        return sp_fig2     
    

# # Define callback to update graph - market share
@callback(
    Output('MS', 'figure'),
    [Input("Product", "value")]
 )    
    
def update_graph_c(Category):
    ms = mer[mer['Product Line']==Category]

    fig3 = px.bar(ms.groupby(['Year','Company'])[['Share']].agg('sum').reset_index(), x="Company", y="Share", animation_frame="Year", animation_group="Company",
               color="Company", color_discrete_sequence=px.colors.qualitative.Pastel1,\
                  hover_name="Company", range_y=[0,100])
    fig3.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
    fig3.update_layout( plot_bgcolor='white', title_text= f'Market Share: {Category}', title_x=0.5, legend=dict(x=1.0, y=1.05))
#                       xaxis={'categoryorder':'array', 'categoryarray':['Brand', "other Brand",'Others']})
    fig3.update_yaxes(showgrid=True, gridwidth=0.3, gridcolor='#ededed')
#     fig3.update_xaxes(showgrid=True, gridwidth=0.3, gridcolor='#ededed')
    
    return fig3




# # Define callback to update graph - Positioning
@callback(
    Output('Pos', 'figure'),
    [Input("Product", "value")]
 )    
    
def update_graph_d(Category):
    rev = ev[ev['Product Line']==Category]


    fig7 = px.scatter(rev.groupby(['Year','Company','Overall Quality'])[['Share']].agg('sum').reset_index(), y="Share", x="Overall Quality",
           size="Share", color="Company", color_discrete_sequence=px.colors.qualitative.Pastel1,\
                  hover_name="Company", size_max=55, range_x=[4,11], range_y=[0,100])

    fig7.update_layout(plot_bgcolor='white', title_text= f'Brand Positioning: {Category}', title_x=0.5, legend=dict(x=1.0, y=1.05))

    fig7.update_yaxes(showgrid=True, gridwidth=0.3, gridcolor='#ededed')
    
    return fig7


# # Define callback to update graph
@callback(
    Output('forecast', 'figure'),
    [Input("years", "value")]
 )


def update_graph_fore(selected_year):
    filtered_df = dffor[dffor['Year'] == selected_year]

#   for no product line
    for_fig = px.histogram(filtered_df, y='Total Price', x='Quarter', color = 'Product Line' , color_discrete_sequence=px.colors.qualitative.Pastel1)
    for_fig.update_layout(barmode='overlay', plot_bgcolor='white',
            title_text= f'Sales Forecast 2024', title_x=0.5, xaxis_title = 'Quarter',yaxis_title='Sales Forecast')
    for_fig.update_xaxes(type='category')

    
    return for_fig


# # Define callback to update graph
@callback(
    Output('forecastpl', 'figure'),
    [Input("years", "value")]
 )

def update_graph_fore2(selected_year):
    filtered_df = dffor[dffor['Year'] == selected_year]

#   for no product line
    for_fig2 = px.histogram(filtered_df, y='Total Price', x='Product Line', color_discrete_sequence=px.colors.qualitative.Pastel1)
    for_fig2.update_layout(barmode='overlay', plot_bgcolor='white',
            title_text= f'Sales Forecast 2024', title_x=0.5, xaxis_title = 'Product Line',yaxis_title='Sales Forecast')
    for_fig2.update_xaxes(type='category')

    
    return for_fig2


# Run app and display result inline in the notebook
# app.run_server(mode='inline', port = 8051)



