var forecast_temperature = JSON.parse(document.currentScript.dataset.forecastTemperature)
var current_time = new Date(document.currentScript.dataset.currentTime)

Highcharts.chart({
    legend: {
        enabled: false,
    },
    chart: {
        renderTo: 'chart-container',
        type: 'areaspline',
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
        marginTop: 50,
        marginBottom: 50,
    },
    title: {
        text: ''
    },
    xAxis: {
        type: 'datetime',
        tickColor: '#1B1B1F',
        tickWidth: 2,
        tickLength: 20,
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
    yAxis: {
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
    },
    series: [{
        name: 'Temperature',
        data: forecast_temperature,
        color: {
            linearGradient : {
                x1: 1,
                y1: 0,
                x2: 0,
                y2: 0
            },
            stops : [
                [0, Highcharts.Color('#5C8CFF').setOpacity(1).get('rgba')],
                [1, Highcharts.Color('#0055D3').setOpacity(1).get('rgba')],
            ]
        },
        fillColor : {
            linearGradient : {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 1,
            },
            stops : [
                [0, Highcharts.Color('#5C8CFF').setOpacity(0.7).get('rgba')],
                [1, Highcharts.Color('#0055D3').setOpacity(0).get('rgba')],
            ]
        },
        pointStart: Date.UTC(current_time.getUTCFullYear(), current_time.getUTCMonth(), current_time.getUTCDate(), current_time.getHours()),
        pointInterval: 3600 * 1000 * 3 // three hour
    }],
    
    plotOptions: {
        series: {
            marker: {
                enabled: true,
                radius: 0.1,
                states: {
                    hover: {
                        radius: 7,
                        lineWidth: 0,
                    },
                },
                symbol: 'diamond'
            },
            shadow: true,
        },
        areaspline: {
            fillOpacity: 0.1
        }
    }
});