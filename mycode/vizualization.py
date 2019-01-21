import plotly
import plotly.graph_objs as go
import plotly.plotly as py

import statistics

plotly.tools.set_credentials_file(username='feco16', api_key='Ngq5UcEcez4VVbwwaucC')


def main():
    x = [i for i in range(5, 40)]
    y = statistics.car_number_with_rule(x, 5)

    y_no_rule = statistics.car_number_no_rule(x, 5)
    mydata = go.Scatter(x=x, y=y, mode='lines',
                        name='With rule. Average: {}'.format(round(sum(y) / len(y), 3)),
                        line=dict(
                            width=2,
                            dash='dot'
                        )
                        )

    mydata_no_rule = go.Scatter(x=x, y=y_no_rule, mode='lines',
                                name='No rule. Average: {}'.format(round(sum(y_no_rule) / len(y), 3)),
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
            title='Car number',
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
