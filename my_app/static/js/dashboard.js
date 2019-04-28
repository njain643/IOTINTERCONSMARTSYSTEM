 $(document).ready(function() {
    setInterval(function() {
        $.ajax({
          url: '/getsensordata/',
          type: 'get',
          dataType: 'json',
           success: function(data){
                    if(data.valuesensor1 < 25){
						$('#sensor1').html("<div style='background:green;' class='circle'><p>"+data.valuesensor1
						                    +" - "+data.namesensor1+"</p></div>");
				    }
					else if(data.valuesensor1 > 25 && data.valuesensor1 < 35){
						$('#sensor1').html("<div style='background:yellow;' class='circle'><p>"+data.valuesensor1
						                    +" - "+data.namesensor1+"</p></div>");
						}
					else if(data.valuesensor1 >= 35){
						$('#sensor1').html("<div style='background:red;' class='circle'><p>"+data.valuesensor1
						                    +" - "+data.namesensor1+"</p></div>");
						}
					else {
						$('#sensor1').html("<div style='background:white;' class='circle'><p><small class='text-muted'><em>No Sensor Data</em></small></p></div>");
					}

					if(data.valuesensor2 < 25){
						$('#sensor2').html("<div style='background:green;' class='circle'><p>"+data.valuesensor2
						                    +" - "+data.namesensor2+"</p></div>");
				    }
					else if(data.valuesensor2 > 25 && data.valuesensor2 < 35){
						$('#sensor2').html("<div style='background:yellow;' class='circle'><p>"+data.valuesensor2
						                    +" - "+data.namesensor2+"</p></div>");
						}
					else if(data.valuesensor2 >= 35){
						$('#sensor2').html("<div style='background:red;' class='circle'><p>"+data.valuesensor2
						                    +" - "+data.namesensor2+"</p></div>");
						}
					else {
						$('#sensor2').html("<div style='background:white;' class='circle'><p><small class='text-muted'><em>No Sensor Data</em></small></p></div>");
					}

					if(data.valuesensor3 < 25){
						$('#sensor3').html("<div style='background:green;' class='circle'><p>"+data.valuesensor3
						                    +" - "+data.namesensor3+"</p></div>");
				    }
					else if(data.valuesensor3 > 25 && data.valuesensor3 < 35){
						$('#sensor3').html("<div style='background:yellow;' class='circle'><p>"+data.valuesensor3
						                    +" - "+data.namesensor3+"</p></div>");
						}
					else if(data.valuesensor3 >= 35){
						$('#sensor3').html("<div style='background:red;' class='circle'><p>"+data.valuesensor3
						                    +" - "+data.namesensor3+"</p></div>");
						}
					else {
						$('#sensor3').html("<div style='background:white;' class='circle'><p><small class='text-muted'><em>No Sensor Data</em></small></p></div>");
					}

            },
            error: function(){
                console.log("error")
            }
        });
       }, 3000);
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function(){
 $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
      $(".button-status").click(function(){
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: $(this).attr('data-url'),
            success: function(url){
               if(url.response == 'ON'){
                    if( url.control == 'blrfan'){
                         $('#'+url.control+"status").html('<p style="color:green;font-weight: bold;">ON</p>');}
                         }
                else if(url.response == 'OFF'){
                    if(url.control == 'blrfan'){
                         $('#'+url.control+"status").html('<p style="color:red;font-weight: bold;">OFF</p>');}
                }
            },
            error: function(xhr, status, e) {
                alert(status, e);
            }
        });
      });
});