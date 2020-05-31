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
});
