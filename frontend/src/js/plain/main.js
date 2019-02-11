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
}