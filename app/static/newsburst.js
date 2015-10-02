$(document).ready(function() {
    console.log("ready!");
	$("#restart").click(function(){
		$.post( "/record_speed", $( "#wpm" ).val() );
	})

	$("#about_text").hide();

	$("#toggle_button").click(function(){
		$("#about_text").toggle("fast");
		
	})


});


$(document).on('click', '.refresh', function(){
	console.log('Entering AJAX get method...')
	$.get('/stories/import', function(data) {
		console.log(data)
		console.log('replacing html')
		$("#top_story_table").html(data);
	});
	return false
});

// $(document).on('click', '.load_link', function(){
// 	console.log('Entering LOAD method...');
// 	link = $(this).attr('name');
// 	console.log(link);
// 	$.get(link, function(data) {

// 		console.log(data)

// 		$("#loaded_story").html(data);
// 	// 	console.log('replacing html')
// 	// 	$("#top_story_table").html(data);
// 	});
// 	return false
// });

// $('#save').submit(function(){
// 	console.log('Entering SAVE method...');
// 	consolg.log($(this))

// 	// $.post('/save_story', function(data) {

// 	// 	console.log(data)

// 	// 	$("#loaded_story").html(data);
// 	// // 	console.log('replacing html')
// 	// // 	$("#top_story_table").html(data);
// 	// });
// 	// return false
// });