<html><head> 
<title>Duggan vs Dugeon: WHO IS THE WINNAR?</title> 
<link rel='stylesheet' href='assets/hw11.css' type='text/css' /> 
</head> 
<body> 
 
      <form action="/" method="get"> 
      Enter name:
	  <input type="text" name="candidate" value="" label="candidate">
	  <input type="submit" value="Submit">
      <!-- ><select id="order_key" name="order_key" onchange='this.form.submit()'> -->
      <!-- ><option value='title'>Movie Title</option><option value='year'>Release Date</option><option value='rating'>Rating</option>
      </select> -->
      </form>

  <p>The result is:</p>
  
  The vote is {{result}}.

  {% if result == "too close to call" %}
    Re-examine input <b>{{candidate}}</b>.
  {% endif %}
  

</body></html>