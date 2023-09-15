const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');


signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});




document.getElementById("myform").addEventListener("submit", function(event) {
const Name = document.getElementById("Name").value;
const Email = document.getElementById("Email").value;
const Password = document.getElementById("Password").value;


if (!Name || !Email || !Password) {
alert("All fields are required");

}


});





document.getElementById("myform1").addEventListener("submit", function(event) {
	const email = document.getElementById("email").value;
	const password = document.getElementById("password").value;
	
	
	if (!email || !password) {
	alert("All fields are required");
	
	}
	
	});
	