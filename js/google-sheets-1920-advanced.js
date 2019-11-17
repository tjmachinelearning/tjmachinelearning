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
    var query = new google.visualization.Query('https://spreadsheets.google.com/tq?key=12NkLjtRTn3SqNNk7kTh76EbS-MUSm0ZOo9mLtOKMZto&output=html&usp=sharing');
    query.setQuery('SELECT A, G, H, I, J, K, L, M, N, O label A "Team Name", G "10/2", H "10/9", I "10/23", J "10/30", K "Other", L "10/16 Submission", M "11/13 Submission", N "Attendance", O "Final Score"');
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
