from dash import dash, Input, Output, html
import dash_glue42
from run import server

app = dash.Dash(__name__, server=server, routes_pathname_prefix="/app-b/", external_stylesheets=['/assets/app-common.css'])

app.enable_dev_tools()

app.layout = dash_glue42.Glue42(id="glue42", children=[

    dash_glue42.MethodRegister(id="g42-register-review-message",
                             definition={"name": "ReviewMessage"}, returns=False),

    html.H3("Application B (Notification Click)"),
    html.Hr(),

    html.H4("The text below is received when a notification is clicked:"),
    html.Div(id="message")
])


@app.callback(
    Output("message", "children"),
    Input("g42-register-review-message", "invoke")
)
def review_message_invocation_handler(invoke):
    if invoke is not None:
        # Get the new message from the method arguments.
        args = invoke.get("args", {})
        message = args.get("message", "")

        return message


if __name__ == "__main__":
    app.run_server(debug=True, host="localhost", port="8051")
