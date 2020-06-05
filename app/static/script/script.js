function addToExpression(i){
	document.getElementById('input').value = document.getElementById('input').value + i;
}

function clearInput() { 
	document.getElementById('input').value = '' ;
}

function deleteEle() { 
	str = document.getElementById('input').value;
	document.getElementById('input').value = str.substring(0, str.length - 1);
}

$(document).ready(function(){
	$('[name=io]').click(function() {
		//$('#input').append($(this).val());
		$('#input').val($('#input').val() + $(this).val());
		if ($('#input').html().length > 20) {
			alert("test");
		}
	});

	$('#input').on("keydown", function(e) {
		if(e.which === 13) { // enter key
			e.preventDefault(); // prevents linebreak
			// here you could add your submit call
			$('#fm').submit();
			return false;
		}
	});
});
