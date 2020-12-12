
<!DOCTYPE html>
<html>
<head>

 <script src = "apigateway.js">

  </script>

  
</head>
<body style="background-color:#1a1a1a">
   <!-- input type="text" id = "inputTextField" /-->
   <!-- button id = "b1" onclick="foo()" style="color:white;background-color:blue">SUBMIT</button -->
   <h1 style="color:yellow; font-family: Helvetica ;text-align:center; "> Sentiment Analysis of IMDB reviews using AWS Comprehend,Lambda and API Gateway </h1>

  <center> <textarea rows="15" cols="80" placeholder="Enter your movie review here to check it's sentiment....." id = "inputTextField"></textarea> </center>


 <button style="width:100px;margin:0 50%; padding:10px; position:relative;left:-50px;top:30px; color:black;background-color:yellow;font-family: Helvetica" id = "b1" onclick="foo()" type="submit">SUBMIT</button>
  <br />
  <br />
  <br />
  <div id= "div1" style = "position:relative; text-align:center; color:green; font-size:18px; font-family: Helvetica"></div>
  
 
  

</body>
</html>
