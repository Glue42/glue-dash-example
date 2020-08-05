import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_glue
from run import server

app = dash.Dash(__name__, server=server, routes_pathname_prefix='/app-a/')

app.layout = dash_glue.glue42(id='glue42', children = [
    dash_glue.context(id="app-styling"),

    html.Div(id ="app-wrapper", children = [
        html.H3('Application A (Context Subscription)'),
        html.Hr(),

        html.Div(children = [
            html.Label("Background Color: "),
            dcc.Input(id='bg-color', type='text', value="white", autoComplete="")
        ])
    ])
])

@app.callback(Output('app-styling', 'outgoing'), [Input('bg-color', 'value')])
def update_app_styling_context(value):
    return { "data": { "backgroundColor": value } }

@app.callback(Output('app-wrapper', 'style'), [Input('app-styling', 'incoming')])
def app_styling_context_changed_handler(context):
    if context is not None:
        bg_color = context['data']['backgroundColor']

        return { "backgroundColor": bg_color }

if __name__ == '__main__':
    app.run_server(debug=True, host='localhost', port='8050')

