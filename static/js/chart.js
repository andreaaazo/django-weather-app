Highcharts.chart({
    legend: {
        enabled: false,
    },
    tooltip: {
        enabled: false,
    },
    chart: {
        renderTo: 'chart-container',
        type: 'areaspline',
        scrollablePlotArea: {
            minWidth: 1346,
            scrollPositionX: 1,
            opacity: 0,
        },
        align: "center",
        backgroundColor: '',
        style: {
            fontFamily: 'Inter'
        },
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
            align: "center"
        },
        crosshair: {
            color: 'rgba(92, 140, 255, 0.2)',
            dashStyle: 'longdash'
        },
    },
    yAxis: {
        title: {
            text: 'Temperature &degC',
            align: "low",
        },
        gridLineColor: '#E1E2EC',
    },
    series: [{
        name: 'Temperature',
        data: [1, 3, 4, 2, 3, 5, 1, 3, 4, 5, 4, 10, 3, 5, 3],
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
        pointStart: Date.UTC(2010, 0, 1),
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