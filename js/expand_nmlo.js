// This file is used for competitions
//With 2 sections: Competition Instructions and Competition Procedures
//And within Competition Instructions section, expandable subsections for each specific competition
//Inside compeitions, in order for this expand.js to work, the line <script src="js/expand.js"></script> was necessary
//as well as <section id="______" style="display:none"> ... </section> around expandable content,
//where ______ can be found in each $('#______').toggle(); line below.


$(document).ready(function() {
    $('#whotitle').on('click',function(){
        $('#who').toggle();
    });
    $('#whattitle').on('click',function(){
        $('#what').toggle();
    });
    $('#howtitle').on('click',function(){
        $('#how').toggle();
    });
    $('#contacttitle').on('click',function(){
        $('#contact').toggle();
    });
    $('#eligibilitytitle').on('click',function(){
        $('#eligibility').toggle();
    });
    $('#signuptitle').on('click',function(){
        $('#signup').toggle();
    });
    
});
