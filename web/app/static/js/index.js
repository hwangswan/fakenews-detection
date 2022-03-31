$('#articleSubmit').on('click', function() {
  $('#articleSubmit').prop('disabled', true);

  let articleContent = $('#articleContent').val();

  let request = $.ajax({
    url : 'http://localhost:5000/detect?article_content=' + articleContent,
    type : 'POST',
  });

  request.done(function(response, textStatus, jqXHR) {
    $.each(response.result, function(id, result) {
      let currentItem = $('#' + id);
      currentItem.removeClass('bg-secondary');
      currentItem.removeClass('bg-success');
      currentItem.removeClass('bg-danger');
      currentItem.text('');

      if (result == 1) {
        currentItem.addClass('bg-success');
        currentItem.text('True news');
      }

      else {
        currentItem.addClass('bg-danger');
        currentItem.text('Fake news');
      }
    });
  });

  request.fail(function(jqXHR, textStatus, errorThrown) {
    console.error(textStatus, errorThrown);
  });

  request.always(function() {
    $('#articleSubmit').prop('disabled', false);
  });
});
