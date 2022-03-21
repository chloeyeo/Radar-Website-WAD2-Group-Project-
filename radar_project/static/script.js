function dropDown(){
    document.getElementById("dropDown").classList.toggle("show");
}

window.onclick = function(event){
    if(!event.target.matches('.dropbtn')){
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
              openDropdown.classList.remove('show');
            }
          }
    }
}
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
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

function add_like(){
  document.getElementById("post_like")
}