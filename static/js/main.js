
$( document ).ready(function() {

  $('.stats-block a').click(function(e){
      e.preventDefault();
      var $this = $(this).parent().parent().parent().find('.toggle');
      $this.slideToggle();
  });
  
});