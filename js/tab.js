function openContent(yearName) {
    var i;
    var x = document.getElementsByClassName("yearsched");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    document.getElementById(yearName).style.display = "block";

    document.getElementById("1617toggle").className = "menu__item";
    document.getElementById("1718toggle").className = "menu__item";
    document.getElementById("1819toggle").className = "menu__item";
    document.getElementById(yearName.substring(0,4)+"toggle").className = "menu__item  menu__item--current";

    document.getElementById("1617mobiletoggle").className = "menu__item";
    document.getElementById("1718mobiletoggle").className = "menu__item";
    document.getElementById("1819mobiletoggle").className = "menu__item";
    document.getElementById(yearName.substring(0,4)+"mobiletoggle").className = "menu__item  menu__item--current";
}
