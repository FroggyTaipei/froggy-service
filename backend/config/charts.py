def get_highchart_pie(data, title=''):
    return {
        'chart': {
            'type': 'pie',
            'plotBackgroundColor': None,
            'plotBorderWidth': None,
            'plotShadow': False,
        },
        'title': {
            'text': title,
        },
        'series': [{
            'colorByPoint': True,
            'data': data,
        }],
        'tooltip': {
            'pointFormat': '{series.name}: <b>{point.percentage:.1f}%</b>',
        },
        'plotOptions': {
            'pie': {
                'showInLegend': True,
                'allowPointSelect': True,
                'cursor': 'pointer',
                'dataLabels': {
                    'enabled': True,
                    'format': "<b>{point.name}</b>: {point.percentage:.1f} %",
                    'style': {
                        'color': "(Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black';",
                    },
                },
            },
        },
    }


def get_highchart_line(data, y_title, title=''):
    return {
        'title': {
            'text': title,
        },
        'xAxis': {
            'type': 'datetime',
            'dateTimeLabelFormats': {
                'day': '%m/%e',
                'month': '%Y/%m',
                'year': '%Y',
            },
        },
        'yAxis': {
            'title': {
                'text': y_title,
            },
        },
        'legend': {
            'layout': 'vertical',
            'align': 'right',
            'verticalAlign': 'middle',
        },
        'plotOptions': {
            'series': {
                'label': {
                    'connectorAllowed': False,
                },
            },
        },
        'series': data,
        'responsive': {
            'rules': [{
                'condition': {
                    'maxWidth': 500,
                },
                'chartOptions': {
                    'legend': {
                        'layout': 'horizontal',
                        'align': 'center',
                        'verticalAlign': 'bottom',
                    },
                },
            }],
        },
    }


def get_highchart_word_cloud(data, title=''):
    return {
        'series': [{
            'type': 'wordcloud',
            'data': data,
            'name': '出現次數',
        }],
        'title': {
            'text': title,
        },
    }
