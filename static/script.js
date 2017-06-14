function request_data() {
	$.ajax({
		type: "GET", 
		url: "task/"+document.getElementById("name_input").value,
		success: function(response){
			$('#task_status').html('Task Status: STARTING')
			$('#result').html('')
			taskid = response['taskid'];
			poll(taskid);
		}
	});
}

function poll(taskid) {
	console.log(taskid)
   	timer = setTimeout(function() {
       $.ajax({ 
       		url: "poll/"+taskid,
       	    success: function(response) {
            	console.log(response)
            	$('#task_status').html('Task Status: ' + response['state'])
            	if (response['state'] == "SUCCESS") {
            		clearInterval(timer);
            		$('#result').html('Result: ' + response['data']['name'])
            	}
       		}, 
       		dataType: "json", 
       		complete: poll(taskid) 
   		});
    }, 10000);
}



