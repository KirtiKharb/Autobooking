$(document).ready(function () {

	var nowDate = new Date();
	var today = new Date(nowDate.getFullYear(), nowDate.getMonth(), nowDate.getDate(), 0, 0, 0, 0);
	$('.datetimepicker').datetimepicker({
		format: "yyyy-mm-dd",
		minView: 2,
		minDate: 0,
		startDate: today,
		showButtonPanel: true,
		autoclose: true,
	}).datetimepicker( "setDate" ,new Date() );

	$('#submit').click(function(event){
		event.preventDefault();
		$.ajax({
			url: "/flight-list/",
			type: "get",
			data: {
				source: $('#basic-addon1').val().substr(-4,3),
				destination: $('#basic-addon2').val().substr(-4,3),
				date_of_flight: $('.datetimepicker').val(),
				number_of_passengers: $('#travel_no').val(),
				travel_class: $('#travel_class').val()
			},
			success: function (resp) {
				$("#mytext").html('');
             	$("#mytext").append("<thead><tr><th>Flight id</th><th>Source</th><th>Destination</th><th>Airline</th><th>Arrival at</th><th>Departure at</th><th>Travel type</th><th>Book flight</th></tr></thead><tbody>");
             	$.each(resp,function(k, record) {
                	$("#mytext").append("<tr><td>"+record.flight_id+"</td><td>"+record.source+"</td><td>"+record.destination+"</td><td>"+record.airline+"</td><td>"+record.arrival_at+"</td><td>"+record.departure_at+"</td><td>"+record.travel_type+"</td><td><a href='/autobook/flightDetails/?flight_id="+record.flight_id+"'>Book</a></td></tr>");
                });
             	$("#mytext").append("</tbody>");
			}
		});	
	});

/*
	function getCookie(name) {
    	var cookieValue = null;
    	if (document.cookie && document.cookie != '') {
        	var cookies = document.cookie.split(';');
        	for (var i = 0; i < cookies.length; i++) {
            	var cookie = jQuery.trim(cookies[i]);
            	// Does this cookie string begin with the name we want?
            	if (cookie.substring(0, name.length + 1) == (name + '=')) {
                	cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                	break;
            	}
        	}
    	}
    	return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');
*/

	var availableSource = [
		{ "id":"2","value":"Singapore Changi International Airport, Singapore (SIN)", "label": "Singapore Changi International Airport, Singapore (SIN)"},
		{"id":"4", "value":"Bengaluru International Airport , Bangalore (BLR)","label": "Bengaluru International Airport , Bangalore (BLR)"},
		{"id":"5", "value":"Indira Gandhi International Airport ,New Delhi (DEL)", "label": "Indira Gandhi International Airport ,New Delhi (DEL)"}
    ];

    $( ".source-autocomplete" ).autocomplete({
      source: availableSource
    });

    $("#basic-addon1").blur(function(){
    	$("#source").val($(this).val());
    });

	$("#basic-addon2").blur(function(){
    	$("#destination").val($(this).val());
    });    

	$("#travel_no").blur(function(){
    	$("#number_of_passengers").val($(this).val());
    });

	$("#travel_class1").blur(function(){
    	$("#travel_class").val($(this).val());
    });

    $("#date").blur(function(){
    	$("#date_of_flight").val($(this).val());
    });

	$("#button4").click(function(){
		var formdata = $('#box').serialize();
        $.ajax({
        	type: "POST",
        	url: "/autobook/autobookRequest/",
        	data: formdata,
        	 /*{
        		"csrfmiddlewaretoken": '',
        		"travel_class": "E",
        		"number_of_passengers": 2,
        		"minimum_price": 4000,
        		"maximum_price": 8000,
        		"date_of_flight": "2014-12-12",
        		"user_email": "1",
        		"destination": "1",
        		"source": "2",
        		}*/
        	success: function(){ alert("Your request is registered. You will receive an email when the price is right."); }
        });
    });

});