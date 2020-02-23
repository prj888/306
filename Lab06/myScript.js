function myFunction(){
	document.getElementById("demo").innerHTML = "Paragraph changed.";
	window.alert("Hello")
	var text;
	var person = prompt("Hello who are you?", "Steve");
	if (person == null || person == ""){
		text  = "You canceled the process!";
	} else{
		text = "Hello" + person;
	}
	document.getElementById("demo").innerHTML = text;
	}
