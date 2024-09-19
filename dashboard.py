

import pandas as pd 
from dash import Dash, html, dcc, Output, Input
import plotly.express as px

app = Dash(__name__)

df = pd.read_excel("consulta_alunos.xlsx")

fig = px.bar(df, x="Bairro", y="Situação", color="Situação", barmode="group")

opcoes = list(df['Situação'].unique())

opcoes.append("Todos")

app.layout = html.Div(children=[ 
    html.H1(children="Fila de Espera Caieiras"),
    dcc.Dropdown(opcoes, value="Todos", id="FiladeEspera"),
    dcc.Graph(
        id="GraficoFilaDeEspera",
        figure=fig
        )
])

@app.callback(
    Output('GraficoFilaDeEspera', 'figure'), #chamando o grafico e a figura do grafico
    Input('FiladeEspera', 'value')
) # callback funcionalidade para atualizar o grafico conforme o filtro 

def update_output(value):

    #varificando se o valor do input é todos 
    if value == 'Todos':
        fig = px.bar(df, x="Bairro", y="Situação", color="Situação", barmode="group")
    else:
        fitroSituacao = df.loc[df['Situação'] == value, :]
        fig = px.bar(df, x="Bairro", y="Situação", color="Situação", barmode="group")


    return fig

if __name__ == '__main__':
    app.run(debug=True)