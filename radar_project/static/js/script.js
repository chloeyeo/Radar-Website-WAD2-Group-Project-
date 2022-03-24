function dropDown(){
  var x = document.getElementById("dropdownprof");
  
  if(x.style.visibility == "visible"){
    document.getElementById("dropdownprof").style.visibility = "hidden";
    document.getElementById("dropdownprof").style.opacity = "0";
  }
  else{
    document.getElementById("dropdownprof").style.visibility = "visible";
  document.getElementById("dropdownprof").style.opacity = "1";
  }
}

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}
function show(){
  document.getElementById("dropbtn").style.background = "blue"

}

function closeNav() {
  
  document.getElementById("mySidenav").style.width = "0";
}

var x = 0;
function openSearch(){
  if (x == 0) {
  document.getElementById("bar").style.width = "300px";
  document.getElementById("bar").style.borderColor = "black";
  x=1; 
  }
  if(x==1){
    
  x=0;
  }

}
