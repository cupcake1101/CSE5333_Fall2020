<?php header('Access-Control-Allow-Origin: *');
?>

<!DOCTYPE html>
<html>
<head>

	<script>

    

     var xhttp = new XMLHttpRequest();


     


     xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    //alert(this.responseText);
   // document.getElementById("div1").innerHTML = this.responseText;
   var responseText = this.responseText;
   if(responseText == "-1"){
   document.getElementById("div1").innerHTML =  "The review is NEGATIVE";
   }
   if(responseText == "1"){
   document.getElementById("div1").innerHTML =  "The review is POSITIVE";
   }

  }
};

	
  function foo(){

    xhttp.open("POST", "/predict", true);

    

    xhttp.setRequestHeader("Content-Type", "application/json");

    var p = document.getElementById("inputTextField").value;




   var name = JSON.stringify({"input": p });

    xhttp.send(name);
  }

  /*
  var xhr = new XMLHttpRequest();
xhr.open("POST", '/server', true);

//Send the proper header information along with the request
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

xhr.onreadystatechange = function() { // Call a function when the state changes.
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        // Request finished. Do processing here.
    }
}
xhr.send("foo=bar&lorem=ipsum");
// xhr.send(new Int8Array()); 
// xhr.send(document);*/


  

	</script>
	
</head>
<body>
  <input type="text" id = "inputTextField" />
	<button id = "b1" onclick="foo()" style="color:white;background-color:blue">SUBMIT</button>
  <br />
  <br />
  <br />
  <div id= "div1"></div>

</body>
</html>
