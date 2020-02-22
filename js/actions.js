// Instagram
var feed = new Instafeed({
	// template: '<img src="{{image}}" />',
    template: '<a href="{{link}}" target="_blank" class="inst-container"><img src="{{image}}" /><div class="inst-positioner"><div class="caption">{{caption}}</div><img src="img/svg/heart.svg"><div class="like-count">{{likes}}</div></div></a>',
    resolution: 'standard_resolution',
    limit: 3,
    get: 'user',
    userId: 5730481341, // Ex: 1374300081
    accessToken: '5730481341.4ce16d6.e427d9a39d1c43869e101249e075ac9a',
    after: function() {
        // disable button if no more results to load
        if (!this.hasNext()) {
            feedLoad.css('display','none')
        }
      },    
  });
  feed.run();

var feedLoad = $('#instafeed-load');
feedLoad.click(function(){
    feed.next()
    if(!feed.hasNext()){ 
        feedLoad.unbind('click');    
        feedLoad.css('display','none')
    }
});

// Google reviews
jQuery(document).ready(function( $ ) {
$("#google-reviews").googlePlaces({
        placeId: 'ChIJL3HjDEFT10ARgEvTaqKJTAk' //Find placeID @: https://developers.google.com/places/place-id
    , render: ['reviews']
    , min_rating: 0
    , max_rows: 3
});
});

 $( function() {
  var $gallery = $('.gallery').flickity({
    cellSelector: '.gallery-cell'
  })  
});  


// Set-up
var navbar = $(".navbar");
var navbar_sections =  $('.navbar-sections');
var navbar_item = $(".navbar-item"); 

var overlay = $(".overlay");

// var home_icon = $("#home");
// var lang_icon = $("#lang");
var toggle_icon = $("#navbar-toggle");

var svg = $(".reset-svg");
var labels = $(".item-label"); 


// On page load
document.querySelector('#navbar-toggle').addEventListener('click', navToggle);
overlay.bind("click", navToggle);
resetNavbarStyle();
toHover();

$( window ).resize(onResize);
$( window ).scroll(onScroll); 

// Scrolling
var ignoreScroll = false; 
var prevScroll = 0; // should start at 0
var treshhold = 0;

function onScroll() {
    if(!ignoreScroll){    
        var scroll = $(window).scrollTop();
        if(scroll>200){
            if(scroll > prevScroll) { // scrollDown     
                treshhold+=1;
                if(treshhold>50){
                    navbar.addClass("hidden"); 
                }           
            } else { // scrollUp        
                treshhold = 0;
                navbar.removeClass("hidden");    
                stickyNavbar(); 
            }
        }
        else if (scroll==0){  // Why did I use toggle here?
            defaultNavbar();
        }        
        prevScroll = scroll;
    }
}

// Menu 
var toggle = false;

function navToggle() {
    if( !toggle ){ openOverlay(); } else{ closeOverlay(); } 
    toggle = !toggle;
}

function resetNavbarStyle(){
    if($(window).scrollTop()<100){ defaultNavbar();} else{ stickyNavbar(); }
} 


// How to open / close ?
function openOverlay(){ 
    toggle_icon.text('✕'); 
    navbar.addClass("navbar-open")     
    navbar_sections.css("display","block");   
    overlay.removeClass("hidden"); 
    toClick();
    stickyNavbar(); 
    ignoreScroll=true;
}
function closeOverlay(){        
    toggle_icon.text('☰');    
    navbar.removeClass("navbar-open");    
    navbar_sections.css("display","");   
    overlay.addClass("hidden"); 
    toHover();
    unclickSiblings(navbar_item);
    resetNavbarStyle();
    ignoreScroll=false;
}


// React to different width 
function onResize() {
    if ($(window).width() <= 990) { // need to close earlier, or some weird shit starts 
        if( toggle ) { 
            openOverlay();  // weird behavior
        }
    } else {       
        closeOverlay();   
        // toggle = false;
    }
}

function toHover() {
    navbar_item.unbind('click');     // remove click 
    navbar_item.hover(function() {    
        $(this).children().css("display","block");       
        $(this).children().css("color",hover_color);     
    }, function() { 
        $(this).children().css("display",'');
        $(this).children().css("color","");
    }); 
    
    // home_icon.unbind('click');
} 


function toClick() {
    navbar_item.unbind('mouseenter mouseleave') // remove hover

    var prev =-1;
    navbar_item.click(function(){
        var curr = this;
        if(prev!=curr){ 
            $(this).find(".item-content").css("display","block");
            $(this).find(".item-label").css("color",hover_color);    
            unclickSiblings($(this));
            prev = curr;
        } else{ 
            // $(this).find(".item-content").css("display","");    // this causes issues         
            // $(this).find(".item-label").css("color","");
            // prev = -1;
        }     
    });  
    // home_icon.bind("click", navToggle(); ); // home button was causing issues 
}

function unclickSiblings(root){
    root.siblings().children().css("display",'');
    root.siblings().children().css("color","");
}


// Navbar styles
// Probably need to refactor this... 
var hover_color;

function stickyNavbar(){
    hover_color = "#b3b3b3";
    navbar.addClass("navbar-sticky");  
    navbar_item.css('color', 'white');  
 
    labels.removeClass("white");
    labels.addClass("blue");

    svg.removeClass("white-svg");
    svg.addClass("blue-svg");  
}

function defaultNavbar(){
    hover_color = "white";
    navbar.removeClass("navbar-sticky");
    navbar_item.css('color', '');
    
    svg.removeClass("blue-svg");  
    svg.addClass("white-svg");
    labels.addClass("white");
    labels.removeClass("blue");
}




// Prevent scrolling on mobile device. 
// https://stackoverflow.com/questions/41594997/ios-10-safari-prevent-scrolling-behind-a-fixed-overlay-and-maintain-scroll-posi

// (function () {
//     var _overlay = document.getElementById('overlay');
//     var _clientY = null; // remember Y position on touch start

//     _overlay.addEventListener('touchstart', function (event) {
//         if (event.targetTouches.length === 1) {
//             // detect single touch
//             _clientY = event.targetTouches[0].clientY;
//         }
//     }, false);

//     _overlay.addEventListener('touchmove', function (event) {
//         if (event.targetTouches.length === 1) {
//             // detect single touch
//             disableRubberBand(event);
//         }
//     }, false);

//     function disableRubberBand(event) {
//         var clientY = event.targetTouches[0].clientY - _clientY;

//         if (_overlay.scrollTop === 0 && clientY > 0) {
//             // element is at the top of its scroll
//             event.preventDefault();
//         }

//         if (isOverlayTotallyScrolled() && clientY < 0) {
//             //element is at the top of its scroll
//             event.preventDefault();
//         }
//     }

//     function isOverlayTotallyScrolled() {
//         // https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollHeight#Problems_and_solutions
//         return _overlay.scrollHeight - _overlay.scrollTop <= _overlay.clientHeight;
//     }
// }())
