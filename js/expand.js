// This file was used for the old submit.html (Called Updates)
//With 3 expandable sections: Competition Instructions, Competition Procedures, and Club Updates
//And within Competition Instructions section, expandable subsections for each specific competition
//Inside submit.html, in order for this expand.js to work, the line <script src="js/expand.js"></script> was necessary
//as well as <section id="______" style="display:none"> ... </section> around expandable content,
//where ______ can be found in each $('#______').toggle(); line below.


$(document).ready(function() {
    $('#comptitle').on('click',function(){
        $('#comp').toggle();
    });
    $('#svmtitle').on('click',function(){
        $('#svm').toggle();
    });
    $('#rftitle').on('click',function(){
        $('#rf').toggle();
    });
    $('#firsttitle').on('click',function(){
        $('#first').toggle();
    });
    $('#standardtitle').on('click',function(){
        $('#standard').toggle();
    });
    $('#updatestitle').on('click',function(){
        $('#updates').toggle();
    });
    $('#nntitle').on('click',function(){
        $('#nn').toggle();
    });
    $('#cnntitle').on('click',function(){
        $('#cnn').toggle();
    });
    $('#kaggletitle').on('click',function(){
        $('#kaggle').toggle();
    });
});
