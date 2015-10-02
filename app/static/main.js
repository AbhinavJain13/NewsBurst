	$(document).ready(function()
	{  
		var wpm = 1;
		$('#go').on('click', function() {
			if($('#go').html() == "Start") {
			  wpm = parseInt($('#wpm').val(), 10);
			  $("#go").html('Pause');
				ospritz.init($('#text'), wpm, $('#word'));
			} else if ($('#go').html() == "Pause") {
				$("#go").html('Resume');
			  ospritz.pause();
			} else if ($('#go').html() == "Resume") {
				$("#go").html('Pause');
			  ospritz.resume();
			}
			
		});
		$('#restart').on('click', function() {
			  ospritz.pause();
			  ospritz.abort();
			  wpm = parseInt($('#wpm').val(), 10);
			  $("#go").html('Pause');
				ospritz.init($('#text'), wpm, $('#word'));
		});
		
		$(document).keydown(function(e) {
      if (e.which == 32){//space bar
      	var a = e.target;
      	var b = $('#text')[0];
      	if (a != b) {
          e.preventDefault();
          if ($('#go').html() == "Pause") {
			  	  $("#go").html('Resume');
			      ospritz.pause();
		    	} else if ($('#go').html() == "Resume") {
		  	  	$("#go").html('Pause');
	  		    ospritz.resume();
  			  }
        }
      } else if (e.which == 37){//left arrow
      	var a = e.target;
      	var b = $('#text')[0];
      	if (a != b) {
          e.preventDefault();
          ospritz.left();
        }
      } else if (e.which == 39){//right arrow
      	var a = e.target;
      	var b = $('#text')[0];
      	if (a != b) {
          e.preventDefault();
          ospritz.right();
        }
      } else if (e.which == 38){//up arrow
      	var a = e.target;
      	var b = $('#text')[0];
      	if (a != b) {
          e.preventDefault();
          ospritz.up();
        }
      } else if (e.which == 40){//down arrow
      	var a = e.target;
      	var b = $('#text')[0];
      	if (a != b) {
          e.preventDefault();
          ospritz.down();
        }
      }   
    });
    $('#text').focus();
	});