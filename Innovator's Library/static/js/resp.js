btn = document.querySelector("#search-box")
function ser() {
    alert("You Typed : " + btn.value)
}
var inp = document.getElementById("search-box")
inp.addEventListener("keyup", function (ele) {
    if (ele.keyCode === 13) {
        ser();
    }

})







header = document.getElementById("header");

window.onscroll = function () { scrollFunction() };
let lang = document.querySelector(".languages")
let sec1 = document.querySelector(".mainsec")
let voide = document.querySelector(".voide")



function scrollFunction() {
    if (header.style.display=="none") {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            header.style.display = "block";
            sec1.classList.add("bg")
            //   header.classList.add("bg")
        } else {
            header.style.display = "none";
            sec1.classList.remove('bg');
            // header.classList.remove('bg');

        }
    }
    else {
        if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
            lang.style.display = "block";
            voide.style.display = "none";
            // sec1.classList.add("bg")
            //   header.classList.add("bg")
        } else {
            lang.style.display = "none";
            voide.style.display = "block";
            //   sec1.classList.remove('bg');
            // header.classList.remove('bg');

        }
    }
}

function myFunction(x) {
    x.classList.toggle("change");
}