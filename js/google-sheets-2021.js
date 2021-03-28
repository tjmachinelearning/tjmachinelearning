/*!
 *
 * Google Sheets To HTML v0.9a
 *
 * To use, simply replace the "tq?key=" value in the
 * URL below with your own unique Google document ID
 *
 * The Google document's sharing must be set to public
 *
 * For privacy purposes, remove the Google document ID
 * at the end of each year, and comment out query.send()
 * Replace the full rankings at year's end with a list
 * of the top three students.
 */

google.load('visualization', '1', {
    packages: ['table']
});
var visualization;

function drawVisualization() {
//     var query = new google.visualization.Query('https://docs.google.com/spreadsheets/d/1BbZ6ddViIMufL0mj3NMDkljT7QlmQYxlZZe26y6L254/edit?usp=sharing');
//     var query = new google.visualization.Query('https://spreadsheets.google.com/tq?key=1BbZ6ddViIMufL0mj3NMDkljT7QlmQYxlZZe26y6L254&output=html&usp=sharing');
//     query.setQuery('SELECT A, B, C, D, E, F label A "Name", B "Decision Trees/Random Forests", C "Support Vector Machines", D "Neural Networks" E "Convolutional Neural Networks", F "Total"');
    var query = new google.visualization.Query('https://spreadsheets.google.com/tq?key=1e6Fpo3WnBqhIcU1wx4q9IvDdizmHDo98v9aNVWEdJfU&output=html&usp=sharing');
    query.setQuery('SELECT A, B, C, D, E, F, G, H label A "Name", B "Decision Trees Pset", C "Decision Trees Comp", D "Random Forest Comp", E "SVM Comp", F "Neural Net Comp", G "NN Pset", H "Total"');
    query.send(handleQueryResponse);
}

function handleQueryResponse(response) {
    if (response.isError()) {
        alert('There was a problem with your query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
    }
    var data = response.getDataTable();
    visualization = new google.visualization.Table(document.getElementById('table'));
    visualization.draw(data, {
        legend: 'bottom'
    });
}
google.setOnLoadCallback(drawVisualization);
