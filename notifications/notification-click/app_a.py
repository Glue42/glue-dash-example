from dash import dash, Input, Output, State, html, dcc
import dash_glue42
from run import server

app = dash.Dash(__name__, server=server, routes_pathname_prefix="/app-a/", external_stylesheets=['/assets/app-common.css'])

app.enable_dev_tools()

app.layout = dash_glue42.Glue42(id="glue42", children=[
    dash_glue42.Notifications(id="g42-notifications"),

    html.H3("Application A (Notification Click)"),
    html.Hr(),

    html.Div(
        [
            html.Label("Message: "),
            dcc.Input(id="message", type="text",
                      value="Check your portfolio!"),
            html.Button(id="raise-notification", children="Raise Notification")
        ]
    )
])


@app.callback(
    Output("g42-notifications", "raise"),
    Input("raise-notification", "n_clicks"),
    State("message", "value"),
    prevent_initial_call=True
)
def raise_notification(_, message):

    # To use the method "ReviewMessage" for handling the notification click,
    # we need to define a settings object and assign it to clickInterop of the notifications options object.
    interop_settings = {
        "method": "ReviewMessage",
        "arguments": {
            "message": message
        }
    }

    notification_options = {
        "title": "New Message",
        "body": "Click to review",
        "clickInterop": interop_settings
    }

    return notification_options


if __name__ == "__main__":
    app.run_server(debug=True, host="localhost", port="8050")
