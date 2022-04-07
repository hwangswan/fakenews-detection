$('#articleSubmit').on('click', function() {
  // Disable submit button
  $('#articleSubmit').prop('disabled', true);

  // Remove every validation class and text.
  $('#articleContent').removeClass('is-invalid');
  $('#articleContent-error').text('');

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
    let classificationResult = $('#classificationResult');

    // Remove previous state of classification result.
    classificationResult.text('');
    classificationResult.removeClass('bg-danger');
    classificationResult.removeClass('bg-success');

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

    if (trueCounts > fakeCounts) {
      classificationResult.text('True news');
      classificationResult.addClass('bg-success');
    }
    else {
      classificationResult.text('Fake news');
      classificationResult.addClass('bg-danger');
    }
  });

  // Error happened, set invalid class for textarea
  // and set error message.
  request.fail(function(jqXHR, textStatus, errorThrown) {
    $('#articleContent').addClass('is-invalid');
    $('#articleContent-error').text(jqXHR.responseJSON.message);
  });

  // Always enable submit button afterwards.
  request.always(function() {
    $('#articleSubmit').prop('disabled', false);
  });
});
