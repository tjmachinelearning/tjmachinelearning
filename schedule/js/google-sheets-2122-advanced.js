google.load('visualization', '1', {
    packages: ['table']
});
var visualization;

function drawVisualization() {
    var query = new google.visualization.Query('https://docs.google.com/spreadsheets/d/10K0bJ3j0sRasX-KSze15g69KgbKINrioAZSlKz7MBsw/gviz/tq?output=html&sheet=Advanced');
    query.setQuery('SELECT A, B, C label A "Date", B "Description", C "Course Materials"');
    query.send(handleQueryResponse);
}

function handleQueryResponse(response) {
    if (response.isError()) {
        alert('There was a problem with your query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
    }
    var data = response.getDataTable();
    console.log(data);
    visualization = new google.visualization.Table(document.getElementById('sched'));
    visualization.draw(data);
}
google.setOnLoadCallback(drawVisualization);