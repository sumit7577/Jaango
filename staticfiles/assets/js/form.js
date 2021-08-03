const form1 = document.getElementById("form1");
const form2 = document.getElementById("form2");
const form3 = document.getElementById("form3");
const form4 = document.getElementById("form4");
const head1 = document.getElementById("1");
const head2 = document.getElementById("2");
const head3 = document.getElementById("3");
const head4 = document.getElementById("4");


form2.style.display = "none";
form3.style.display = "none";
form4.style.display = "none";
const button1 = document.getElementById("form1Button");
const button2 = document.getElementById("form2Button");
const button3 = document.getElementById("form3Button");
const button4 = document.getElementById("form4Button");

const inputs = form1.getElementsByTagName("input")
const errors1 = form1.getElementsByClassName("text-error");
const styles1 = form1.getElementsByClassName("input");

const inputs2 = form2.getElementsByTagName("select");
const errors2 = form2.getElementsByClassName("text-error");
const styles2 = form2.getElementsByClassName("input");

const inputs3 = form3.getElementsByTagName("select");
const errors3 = form3.getElementsByClassName("text-error");
const styles3 = form3.getElementsByClassName("input");

const inputs4 = form4.getElementsByTagName("input");
const errors4 = form4.getElementsByClassName("text-error");
const styles4 = form4.getElementsByClassName("input");
button4.style.display = "none";

//basic info
button1.addEventListener("click", function ok(e) {
    let variable = 0;
    for (let i = 0; i < inputs.length; i++) {
        if (inputs[i].value != "") {
            variable++;
        }
    }
    console.log(variable);
    if (variable == inputs.length) {
        form1.style.display = "none";
        form2.style.display = "block";
        form3.style.display = "none";
        form4.style.display = "none";
        head1.classList.remove("activa");
        head2.classList.add("activa");
    }
    else {

        for (let i = 0; i < errors1.length; i++) {
            errors1[i].innerHTML = "This field is required";
            for (let k = 0; k < styles1.length; k++) {
                styles1[k].style.borderColor = "red";
            }
        }
    }
}
);

//availability
button2.addEventListener("click", function first(e) {
    let success1 = false;
    for (let i = 0; i < inputs2.length; i++) {
        if (inputs2[i].required && inputs2[i].value == "") {
            break;
        }
        else {
            success1 = true;
            form1.style.display = "none";
            form2.style.display = "none";
            form3.style.display = "block";
            form4.style.display = "none";
            head3.classList.add("activa");
            head2.classList.remove("activa");
        }
    }
    if (success1 == false) {
        for (let i = 0; i < errors2.length; i++) {
            errors2[i].innerHTML = "This field is required";
            for (let k = 0; k < styles2.length; k++) {
                styles2[k].style.borderColor = "red";
            }
        }
    }

}
);

//amenities
button3.addEventListener("click", function second(e) {
    let success2 = false;
    for (let i = 0; i < inputs3.length; i++) {
        if (inputs3[i].required && inputs3[i].value == "") {
            break;
        }
        else {
            success2 = true;
            form1.style.display = "none";
            form2.style.display = "none";
            form3.style.display = "none";
            form4.style.display = "block";
            head4.classList.add("activa");
            head3.classList.remove("activa");
            button4.style.display = "block";
        }
    }
    if (success2 == false) {
        for (let i = 0; i < errors3.length; i++) {
            errors3[i].innerHTML = "This field is required";
            for (let k = 0; k < styles3.length; k++) {
                styles3[k].style.borderColor = "red";
            }
        }
    }

}
);

//preferance
console.log(button4.type);
button4.addEventListener("click", function third(e) {
    let success3 = 0;
    for (let i = 0; i < inputs4.length; i++) {
        console.log(inputs4[i]);
        if (inputs4[i].value != "") {
            success3++;
        }
    }
    console.log(success3);
    if (success3 == inputs4.length) {
       button4.type = "submit";
    }
    
    else {

        for (let i = 0; i < errors4.length; i++) {
            errors4[i].innerHTML = "This field is required";
            for (let k = 0; k < styles4.length; k++) {
                styles4[k].style.borderColor = "red";
            }
        }
    }
}
);