 
 

//  nav barr-------------------------------

const navToggler =document.querySelector('.menu-icon');
const navItems = document.querySelector('.nav-items');

navToggler.addEventListener('click',navToggle);

function navToggle(){
  navItems.classList.toggle('active')
}




//  offer section  imgae slide -----------------
 
 let slides =document.querySelectorAll('.slide-container');
 let index = 0;
 function next(){
    slides[index].classList.remove('active');
    index=(index+1) %slides.length;
    slides[index].classList.add('active');
    
 }
 function prev(){
    slides[index].classList.remove('active');
    index=(index-1+slides.length)%slides.length;
    slides[index].classList.add('active');
   
 }
 
function slide(){

   slides[index].classList.remove('active');
   index=(index+1) %slides.length;
   slides[index].classList.add('active');

}

setInterval( slide,4000) 





// search  itemas

const Search =document.querySelector('.search-icon');
const SearchBar=document.querySelector('.search-bar');

Search.addEventListener('click',searchtoggle);

function searchtoggle(){
SearchBar.classList.toggle('active')
}



// product itme slider 
//    for man 

let manslide =document.querySelectorAll('.prod-card');
let manindex = 0;

function sliders(){
   manslide[manindex].classList.remove('active');
   manindex=(manindex+1) % manslide.length;
   manslide[manindex].classList.add('active');
   
}
setInterval( sliders,2000) 



// for woman


let WomanSlide =document.querySelectorAll('.prod-card2');
let WomanIndex = 0;

function SliderWo(){
   WomanSlide[WomanIndex].classList.remove('active');
   WomanIndex=(WomanIndex+1)%WomanSlide.length;
   WomanSlide[WomanIndex].classList.add('active');
   
}
setInterval( SliderWo,2000) 

