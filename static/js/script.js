$(document).ready(function(){
    var dynamicText = ['Programing', 'Python', 'Django','PHP', 'ETC...' ];
    var index = 0;

    $.fn.appendTextToDiv = function(){
        if(index == dynamicText.length){
            index = 0;
        }
        $(".dynamic_text h2").text(dynamicText[index]);
        index++

        setTimeout(function(){
            $.fn.appendTextToDiv();
        }, 2500);
    }
    $.fn.appendTextToDiv();

})

function showProjects() {
    var cb = document.getElementById("toggle");
    var elements = document.getElementsByClassName("brows-projects-buttons");


    if (window.innerWidth <= 700) {
        if (elements.length > 0) {
            var element = elements[0];

            if (cb.checked) {
                element.style.width = "160px";
                element.style.visibility="visible";
            } else {
                element.style.width = "0px";
                element.style.visibility="hidden";
            }
        }
    }else {
        element.style.width = "100%";
        element.style.visibility="visible";
    }

}