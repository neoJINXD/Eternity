function addToExpression(i){
	document.getElementById('resultInput').value = document.getElementById('resultInput').value + i;
}

function clearInput() { 
	document.getElementById('resultInput').value = '' 
}

function delEle() { 
	str = document.getElementById('resultInput').value;
	document.getElementById('resultInput').value = str.substring(0, str.length - 1)
}