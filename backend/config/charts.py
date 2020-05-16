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
            'pointFormat': '<b>{point.percentage:.1f}%</b>',
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
        'chart': {
            'type': 'spline',
        },
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


def get_highchart_packed_bubble(data, title=''):
    print(data)
    return {
        'chart': {
            'type': 'packedbubble',
        },
        'title': {
            'text': title
        },
        'tooltip': {
            'useHTML': 'true',
            'pointFormat': '{point.value}'
        },
        'plotOptions': {
            'packedbubble': {
                'minSize': '30%',
                'maxSize': '150%',
                'layoutAlgorithm': {
                    'splitSeries': False,
                    'gravitationalConstant': 0.02
                },
                'dataLabels': {
                    'enabled': 'true',
                    'format': '{point.name}',
                    'style': {
                        'color': 'black',
                        'textOutline': 'none',
                        'fontWeight': 'normal'
                    }
                }
            }
        },
        'series': data
    }
