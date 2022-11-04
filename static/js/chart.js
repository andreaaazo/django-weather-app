
// Graph
const ctx = document.getElementById("chart").getContext('2d');
const myChart = new Chart(ctx, {
type: 'line',
data: {
    labels: ["00", "03", "06", "09", "11", "13", "16", "19", "22"],
    datasets: [{
    label: 'Last week',
    backgroundColor: 'rgba(161, 198, 247, 1)',
    borderColor: 'rgb(47, 128, 237)',
    data: ["7", "2.2", "2.5", "15", "19", "18", "17", "18", "5"],
    }]
},
options: {
    legend: {
        display: false,
    },
    scales: {
    yAxes: [{
        ticks: {
        beginAtZero: true,
        }
    }]
    }
},
});

console.log("hi")