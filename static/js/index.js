
// //question script

function check1() {
    document.getElementById("r2").style.display = "block";
}

function check2() {
    document.getElementById("r3").style.display = "block";
}

function sub() {
    document.getElementById("r4").style.display = "block";
}

function view() {
    document.getElementById("profileDetails").style.display = "block";
    document.getElementById("zoomindex").style.zIndex = "0";
}

function view1() {
    document.getElementById("profileDetails1").style.display = "block";
    document.getElementById("zoomindex").style.zIndex = "0";
}

function view2() {
    document.getElementById("profileDetails2").style.display = "block";
    document.getElementById("zoomindex").style.zIndex = "0";
}


function view3() {
    document.getElementById("profileDetails3").style.display = "block";
    document.getElementById("zoomindex").style.zIndex = "0";
}

function view4() {
    document.getElementById("profileDetails4").style.display = "block";
    document.getElementById("zoomindex").style.zIndex = "0";
}

function view5() {
    document.getElementById("profileDetails5").style.display = "block";
    document.getElementById("zoomindex").style.zIndex = "0";
}

function closed1() {
    document.getElementById("profileDetails").style.display = "none";
    document.getElementById("zoomindex").style.zIndex = "1";

}
function closed2() {
    document.getElementById("profileDetails1").style.display = "none";
    document.getElementById("zoomindex").style.zIndex = "1";

}
function closed3() {
    document.getElementById("profileDetails2").style.display = "none";
    document.getElementById("zoomindex").style.zIndex = "1";

}
function closed4() {
    document.getElementById("profileDetails3").style.display = "none";
    document.getElementById("zoomindex").style.zIndex = "1";

}
function closed5() {
    document.getElementById("profileDetails4").style.display = "none";
    document.getElementById("zoomindex").style.zIndex = "1";

}

function closed6() {
    document.getElementById("profileDetails5").style.display = "none";
    document.getElementById("zoomindex").style.zIndex = "1";

}

//redirect takeestimate page

function takeestimates() {
    // let signmail = document.getElementById("semail").value;
    // let signpass = document.getElementById("spass").value;
    // let logmail = document.getElementById("lemail").value;
    // let logpass = document.getElementById("lpass").value;

    // if (signmail != logmail && signpass != logpass) {
    //     counter = 1
    //     window.location.assign("signin.html?showdiv=true");

    // } 
    // else{
    //     // counter = 1
    //     // window.location.assign("takeestimatepage.html?showdiv=true");
    //     alert("success")
    // }

    window.location.assign("takeestimatepage.html");
}

function i1(){
    document.getElementById('chimg').src='./img/sofo-3.jpg';
}
function i2(){
    document.getElementById('chimg').src='./img/sofo2.jpg';
}
function i3(){
    document.getElementById('chimg').src='./img/ch-1.jpg';
}
function i4(){
    document.getElementById('chimg').src='./img/ch-3.jpg';
}

//sign-in script

// function newone() {

//     var FirstName = document.getElementById("sfname").value;
//     var Email = document.getElementById("semail").value;
//     var Pass = document.getElementById("spass").value;
//     var Contact = document.getElementById("scontact").value;

//     if (FirstName == '') {
//         alert("Please Enter First Name...")
//         document.getElementsByClassName("signnone").style.display = "block";
//         document.getElementsByClassName("loginnone").style.display = "none";
//     }
//     else if (FirstName.search(/^[a-zA-Z ]+$/) == -1) {
//         alert("Please Enter Valid First Name...")
//         document.getElementsByClassName("signnone").style.display = "block";
//         document.getElementsByClassName("loginnone").style.display = "none";
//     }
//     else if (Email == '') {
//         alert("Please Enter Email...")
//         document.getElementsByClassName("signnone").style.display = "block";
//         document.getElementsByClassName("loginnone").style.display = "none";
//     }
//     else if (Email.search(/^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/) == -1) {
//         alert("Please Enter valid Email...")
//         document.getElementsByClassName("signnone").style.display = "block";
//         document.getElementsByClassName("loginnone").style.display = "none";
//     }
//     else if (Pass == '') {
//         alert("Please Enter Password...")
//         document.getElementsByClassName("signnone").style.display = "block";
//         document.getElementsByClassName("loginnone").style.display = "none";
//     }
//     else if (Contact == '') {
//         alert("Please Enter PhoneNumber...")
//         document.getElementsByClassName("signnone").style.display = "block";
//         document.getElementsByClassName("loginnone").style.display = "none";
//     }
//     else if (Contact.search(/^[0-9 ]+$/) == -1) {
//         alert("Please Enter Valid PhoneNumber...")
//         document.getElementsByClassName("signnone").style.display = "block";
//         document.getElementsByClassName("loginnone").style.display = "none";
//     }
//     else {
//         document.getElementById("signnone").style.display = "none";
//         document.getElementById("loginnone").style.display = "block";
//     }
// }


// // login script

// function log() {

//     let signmail = document.getElementById("semail").value;
//     let signpass = document.getElementById("spass").value;
//     let logmail = document.getElementById("lemail").value;
//     let logpass = document.getElementById("lpass").value;

//     if (logmail === "") {
//         alert("Please Enter Your Registered Email")
//         document.getElementById("loginnone").style.display = "block";
//     } else if (logpass === "") {
//         alert("Please Enter Your Registered Password")
//         document.getElementById("loginnone").style.display = "block";
//     } else if (signmail != logmail) {
//         alert("Please Enter Valid Email")
//         document.getElementById("loginnone").style.display = "block";
//     } else if (signpass != logpass) {
//         alert("Please Enter Valid Password")
//         document.getElementById("loginnone").style.display = "block";
//     } else {
//         document.getElementById("loginnone").style.display = "none";
//         counter = 1
//         window.location.assign("index.html?showdiv=true");
//     }
// }

//select room,hall,kitchen

function custom(){
    document.getElementById("cus1").style.display = "block";
    document.getElementById("cus").style.display = "none";
}

function r1() {
    document.getElementById("ro1").style.display = "block";
    document.getElementById("ro2").style.display = "none";
    document.getElementById("ha1").style.display = "none";
    document.getElementById("ki1").style.display = "none";
}

function r2() {
    document.getElementById("ro1").style.display = "none";
    document.getElementById("ro2").style.display = "block";
    document.getElementById("ha1").style.display = "none";
    document.getElementById("ki1").style.display = "none";
}

function h1() {
    document.getElementById("ro1").style.display = "none";
    document.getElementById("ro2").style.display = "none";
    document.getElementById("ha1").style.display = "block";
    document.getElementById("ki1").style.display = "none";
}

function k1() {
    document.getElementById("ro1").style.display = "none";
    document.getElementById("ro2").style.display = "none";
    document.getElementById("ha1").style.display = "none";
    document.getElementById("ki1").style.display = "block";
}

//redirect the display page

function displaypage() {
    window.location.assign("display.html");
}

function designerpage(){
    window.location.assign("profile_page.html");
}

function paymentpage(){
    window.location.assign("payment.html");
}


function whl1() {
    document.getElementById("whl1.2").style.display = "block";
    document.getElementById("whl1.1").style.display = "none";
}
function whl2() {
    document.getElementById("whl2.2").style.display = "block";
    document.getElementById("whl2.1").style.display = "none";
}
function whl3() {
    document.getElementById("whl3.2").style.display = "block";
    document.getElementById("whl3.1").style.display = "none";
}
function whl4() {
    document.getElementById("whl4.2").style.display = "block";
    document.getElementById("whl4.1").style.display = "none";
}
function whl5() {
    document.getElementById("whl5.2").style.display = "block";
    document.getElementById("whl5.1").style.display = "none";
}
function whl6() {
    document.getElementById("whl6.2").style.display = "block";
    document.getElementById("whl6.1").style.display = "none";
}
function whl7() {
    document.getElementById("whl7.2").style.display = "block";
    document.getElementById("whl7.1").style.display = "none";
}
function whl8() {
    document.getElementById("whl8.2").style.display = "block";
    document.getElementById("whl8.1").style.display = "none";
}


//payment page

function payme() {
    document.getElementById("payme1").style.display = "block";
    document.getElementById("zoomindex").style.zIndex = "0";
}

function paymee() {
    document.getElementById("payme2").style.display = "block";
    document.getElementById("zoomindex").style.zIndex = "0";
}

function closedpay() {
    document.getElementById("payme1").style.display = "none";
    document.getElementById("zoomindex").style.zIndex = "1";

}

function closedpay1() {
    document.getElementById("payme2").style.display = "none";
    document.getElementById("zoomindex").style.zIndex = "1";

}