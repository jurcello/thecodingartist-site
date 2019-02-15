import $ from 'jquery';
import 'jquery.scrollintoview';

function scrollToDiv(div){
  $('html, body').animate({
    scrollTop: $(div).offset().top
  }, 500);
}


export default  () => {
  $("#show-more").click( event => {
    event.preventDefault();
    scrollToDiv($("#scroll-target"));
  });

  $("#scroll-to-top").click(event => {
    event.preventDefault();
    scrollToDiv($(".main").first());
  });

  const hamburger = $("button.hamburger");
  const navMenu = $(".nav__menu");

  hamburger.click(event => {
    event.preventDefault();
    console.log(navMenu)
    if (hamburger.hasClass("is-active")) {
      hamburger.removeClass("is-active");
      navMenu.removeClass("nav__menu--active");
    }
    else {
      hamburger.addClass("is-active");
      navMenu.addClass("nav__menu--active");
    }

  })
}