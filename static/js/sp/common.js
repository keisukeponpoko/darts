$(function() {
  $('.collapse-button').on('click', function() {
    console.log('aa');
    $('.collaspe-list').stop(true, true).slideToggle();
  });
});
