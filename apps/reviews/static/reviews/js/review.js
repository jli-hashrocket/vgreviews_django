$(function (){

  $('.btn.active').click(function(e){
    e.preventDefault();
    var rev_id = $(this).attr('data-attr');
    $.get('/reviews/like', { review_id: rev_id}, function(data){
      $('td#review_' + rev_id).html(data);
    });
  });
});
