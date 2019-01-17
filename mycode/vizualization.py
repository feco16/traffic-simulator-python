import statistics

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='feco16', api_key='Ngq5UcEcez4VVbwwaucC')



def main():

    X = [i for i in range(5, 40)]
    Y = statistics.car_number_with_rule(X, 3)

    Y_no_rule = statistics.car_number_with_rule(X, 3)
    mydata = go.Scatter(x=X, y=Y, mode='lines',
                        name='Rule',
                        line=dict(
                            width=2,
                            dash='dot'
                        )
                        )

    mydata_no_rule = go.Scatter(x=X, y=Y_no_rule, mode='lines',
                        name='No rule',
                        line=dict(
                            width=2,
                            dash='dot'
                        )
                        )

    layout = go.Layout(
        autosize=False,
        width=800,
        height=600,
        title='Traffic simulator',
        xaxis=dict(
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='Speed',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    #
    fig = go.Figure()
    fig.add_traces([mydata, mydata_no_rule])
    fig._layout = layout

    #
    py.plot(fig, filename='traffic-line')


if __name__ == '__main__':
    main()
