google.load('visualization', '1', {
    packages: ['table']
});
var visualization;

function drawVisualization() {
    var query = new google.visualization.Query('https://docs.google.com/spreadsheets/d/1_EwDSD-7_bvCrScRyoMe6reckFCzHZ-exUJw8yTnxoA/gviz/tq?output=html&sheet=Advanced');
    query.setQuery('SELECT A, B label A "Name", B "Pytorch PSET"');
    query.send(handleQueryResponse);
}

function handleQueryResponse(response) {
    if (response.isError()) {
        alert('There was a problem with your query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
    }
    var data = response.getDataTable();
    visualization = new google.visualization.Table(document.getElementById('table2'));
    visualization.draw(data);
}
google.setOnLoadCallback(drawVisualization);