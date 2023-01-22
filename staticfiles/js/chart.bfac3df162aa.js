const forecast_temperature = JSON.parse(document.currentScript.dataset
    .forecastTemperature)
const forecast_icons = JSON.parse(document.currentScript.dataset
    .forecastIcons.replace(/'/g, '"'))
const current_time = new Date(document.currentScript.dataset
    .currentTime)

// Create icons array
var forecast_data_icons = new Array()

forecast_icons.forEach(function(icon) {
    forecast_data_icons.push({
        y: 1,
        color: {
            pattern: {
                image: `https://openweathermap.org/img/wn/${icon}@2x.png`,
                aspectRatio: 1,
            },
        }
    })
})

Highcharts.chart({
    // Legend
    legend: {
        enabled: false,
    },
    // Chart
    chart: {
        renderTo: 'chart-container',
        scrollablePlotArea: {
            minWidth: 4000,
            scrollPositionX: 0,
            opacity: 0,
        },
        align: "center",
        backgroundColor: '',
        style: {
            fontFamily: 'Inter',
        },
        marginTop: 10,
        marginBottom: 50,
    },
    title: {
        text: ''
    },
    // xAxes
    xAxis: {
        type: 'datetime',
        tickColor: '#1B1B1F',
        tickWidth: 2,
        tickLength: 10,
        tickColor: '#E1E2EC',
        tickmarkPlacement: 'between',
        labels: {
            align: "center",
            style: {
                fontSize: 14,
            }
        },
        crosshair: {
            color: 'rgba(92, 140, 255, 0.5)',
            dashStyle: 'longdash'
        },
    },
    // yAxes
    yAxis: [{
        top: "30%",
        height: "70%",
        title: {
            text: 'Temperature &degC',
            align: "low",
        },
        gridLineColor: '#E1E2EC',
        labels: {
            style: {
                fontSize: 14,
            }
        },
    }, {
        top: "0%",
        height: "20%",
        title: {
            enabled: false,
        },
        labels: {
            enabled: false,
        },

        gridLineColor: 'transparent',
    }],
    // Series
    series: [{
        type: 'areaspline',
        yAxis: 0,
        name: 'Temperature',
        data: forecast_temperature,
        color: {
            linearGradient: {
                x1: 1,
                y1: 0,
                x2: 0,
                y2: 0
            },
            stops: [
                [0, Highcharts.Color('#5C8CFF')
                    .setOpacity(1).get('rgba')
                ],
                [1, Highcharts.Color('#0055D3')
                    .setOpacity(1).get('rgba')
                ],
            ]
        },
        fillColor: {
            linearGradient: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 1,
            },
            stops: [
                [0, Highcharts.Color('#5C8CFF')
                    .setOpacity(0.7).get('rgba')
                ],
                [1, Highcharts.Color('#0055D3')
                    .setOpacity(0).get('rgba')
                ],
            ]
        },
        pointInterval: 3600 * 1000 * 3, // three hours
        pointStart: Date.UTC(current_time
            .getUTCFullYear(), current_time
            .getUTCMonth(), current_time
            .getUTCDate(), current_time.getHours()
        ),
        zIndex: 1,
    }, {
        name: 'Icon',
        yAxis: 1,
        type: 'column',
        pointWidth: 110,
        enableMouseTracking: false,
        pointPadding: 0.25,
        borderColor: 'transparent',
        borderWidth: 0,
        data: forecast_data_icons,
        pointInterval: 3600 * 1000 * 3, // three hours
        pointStart: Date.UTC(current_time
            .getUTCFullYear(), current_time
            .getUTCMonth(), current_time
            .getUTCDate(), current_time.getHours()
        ),
    }],
    // Plot options
    plotOptions: {
        series: {
            states: {
                inactive: {
                    opacity: 1
                }
            },
        }
    }
});