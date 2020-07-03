
function onlyUnique(value, index, self) { 
    return self.indexOf(value) === index;
}

var Autocomplete = function(options) {
  this.form_selector = options.form_selector
  this.url = options.url || '/search/spelling/'
  this.delay = parseInt(options.delay || 300)
  this.minimum_length = parseInt(options.minimum_length || 2)
  this.form_elem = null
  this.query_box = null
}

Autocomplete.prototype.setup = function() {
  var self = this;
  this.form_elem = $(this.form_selector);
  this.query_box = this.form_elem.find('input[name=q]');

  // Watch the input box.
  this.query_box.on('keyup', function() {
    var query = self.query_box.val();
    if(query.length < self.minimum_length) { return false };
    self.fetch(query);
  })      
}

Autocomplete.prototype.fetch = function(query) {
  var self = this
  $.ajax({ url: this.url, data: { 'q': query },
    success: function(data) {
      data = data.results;
      if (typeof data.spellcheck.suggestions[query] !== "undefined") {
          var results = data.spellcheck.suggestions[query];
      }
      self.show_results( results )
    }
  })
}

Autocomplete.prototype.show_results = function(data) {
  // Remove any existing results.
  $('.ac-results').remove()

  if (data == undefined) {
    $('.suggestions').html('');        
  } else if (typeof data.suggestion == "undefined") {
    $('.suggestions').html('');        
  } else {
        
    var results = data.suggestion || []
    var results_wrapper = $('<div class="ac-results"></div>')
    var base_elem = $('<div class="result-wrapper"><a href="#" class="ac-result"></a></div>')

    if(results.length > 0) {
      for(var res_offset in results) {
        var elem = base_elem.clone();
        // Don't use .html(...) here, as you open yourself to XSS.
        // Really, you should use some form of templating.
        elem.find('.ac-result').text(results[res_offset].word);
        elem.find('.ac-result').attr('href', '/search/?q=' + results[res_offset].word);
        if (res_offset < results.length - 1) {
          elem.append(', ');
        }
        results_wrapper.append(elem);
      }
      $('.suggestions').html('Suggested spelling: ').append(results_wrapper);
    } else {
      var elem = base_elem.clone()
      elem.text("")
      results_wrapper.append(elem)
      $('.suggestions').html('');
    }

  }
}

$( document ).ready(function() {

  $('.toggle-switch').click(function(e){
      e.preventDefault();
      var $this = $(this).parent().parent().find('.toggle');
      $this.slideToggle();
  });
  
  window.autocomplete = new Autocomplete({ form_selector: '.autocomplete-me' });
  window.autocomplete.setup();

});