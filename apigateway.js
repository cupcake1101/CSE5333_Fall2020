 var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    //alert(this.responseText);
   var responseJson   = this.responseText;
   var obj = JSON.parse(responseJson)
   document.getElementById("div1").innerHTML = "Sentiment:" + obj.Response.Sentiment + "<br />" + "SentimentScore:" + "<br />" +  "POSITIVE: " + obj.Response.SentimentScore.Positive + "<br />" + "NEGATIVE: " + obj.Response.SentimentScore.Negative + "<br />" + "NEUTRAL: " + obj.Response.SentimentScore.Neutral + "<br />" +"MIXED: " +obj.Response.SentimentScore.Mixed ;
	//document.getElementById("div1").innerHTML = responseJson;
  //+ "," obj.Response.SentimentScore.Positive
  }
};

 
  function foo(){

    xhttp.open("POST", "https://izcsaczs14.execute-api.us-east-2.amazonaws.com/dev", true);

   

    //xhttp.setRequestHeader("x-amzn-RequestId", "aa1dd9ea-fa6e-4c10-a085-1bc6f6b68a4e");

     //xhttp.setRequestHeader("x-amz-apigw-id", "WsT7iF6fCYcFY8A=");

      //xhttp.setRequestHeader("X-Amzn-Trace-Id", "Root=1-5fc199e3-398c0ce13610cc9513dd187f;Sampled=0");

    var p = document.getElementById("inputTextField").value;

      

   var name = JSON.stringify( {
   "Text" : p

});

    xhttp.send(name);
  }