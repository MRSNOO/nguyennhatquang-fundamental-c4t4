// alert("Hello C4T4, Im a js script");  // = print
console.log("hello, this is c4t4 logging"); 

var title = "Bye bye";
console.log(title); // print vao console dung ctrl shift r

var m = 23 ;
m--;
console.log(m);

function foo() {
    setTimeout(foo,3000);
    console.log("Bar");
}

var minutes = 2;
var seconds = 0;
var titleminute = document.getElementById("timer_minutes");
var titlesecond = document.getElementById("timer_seconds");


function runner(){
if(seconds == 0){
    if(minutes == 0){
        console.log("Out of time");
        var btnStart = document.getElementById("btn_start");
    btnStart.disabled = false;
    }
    else{
    minutes -= 1;
    seconds = 59;
    setTimeout(runner,10);
    }

}
else{
    seconds -=1;
    setTimeout(runner,10);
}
if (minutes<10){
    titleminute.innerHTML = "0"+ minutes;
}
else{
    titleminute.innerHTML = minutes;  // neu minute hoac second co 1 chu so thi them 0

}

if (seconds<10){
titlesecond.innerHTML = "0"+ seconds;
}
else {
    titlesecond.innerHTML = seconds;
}
console.log(minutes);
console.log(seconds);

// setTimeout(runner,1000); //de quy cu 1 giay chay ham runner
}

console.log("Start");

function onStartClick(){
    var titleContent = document.getElementById("title_content"); //search ca file html 
    titleContent.innerHTML = "Timer Running"; //thay noi dung trong the
    console.log(titleContent);
    var btnStart = document.getElementById("btn_start");
    btnStart.disabled = true;
    minutes = 2;
    seconds = 0;
    runner(); // khi click vao start thi chay runner 
    
}
//khoi dong lai phai giu shift