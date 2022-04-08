$('#articleSubmit').on('click', function() {
  // Disable submit button
  $('#articleSubmit').prop('disabled', true);

  // Remove every validation class and text.
  $('#articleContent').removeClass('is-invalid');
  $('#articleContent').removeClass('is-valid');

  $('#articleContent-message').removeClass('invalid-feedback');
  $('#articleContent-message').removeClass('valid-feedback');
  $('#articleContent-message').text('');

  // Get article content
  let articleContent = $('#articleContent').val();

  // Send AJAX request.
  let request = $.ajax({
    url : '{{ url_for("detect") }}',
    type : 'POST',
    data : {
      'article_content' : articleContent
    }
  });

  // Request success without any errors.
  request.done(function(response, textStatus, jqXHR) {
    let trueCounts = 0, fakeCounts = 0;

    $.each(response.result, function(id, result) {
      let currentItem = $('#' + id);
  
      currentItem.removeClass('bg-secondary');
      currentItem.removeClass('bg-success');
      currentItem.removeClass('bg-danger');
      currentItem.text('');

      if (result == 1) {
        currentItem.addClass('bg-success');
        currentItem.text('True news');
        ++trueCounts;
      }

      else {
        currentItem.addClass('bg-danger');
        currentItem.text('Fake news');
        ++fakeCounts;
      }
    });

    // Conclusion
    if (trueCounts > fakeCounts) {
      $('#articleContent').addClass('is-valid');
      $('#articleContent-message').addClass('valid-feedback');
      $('#articleContent-message').text('This could be a True News');
    }

    else {
      $('#articleContent').addClass('is-invalid');
      $('#articleContent-message').addClass('invalid-feedback');
      $('#articleContent-message').text('This could be a Fake News');
    }
  });

  // Error happened, set invalid class for textarea
  // and set error message.
  request.fail(function(jqXHR, textStatus, errorThrown) {
    $('#articleContent').addClass('is-invalid');
    $('#articleContent-message').addClass('invalid-feedback');
    $('#articleContent-message').text(jqXHR.responseJSON.message);
  });

  // Always enable submit button afterwards.
  request.always(function() {
    $('#articleSubmit').prop('disabled', false);
  });
});
