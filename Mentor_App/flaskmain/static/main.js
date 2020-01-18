$(document).ready(function() {
  console.log("ready!");

$(function() {
    var $wrapper = $('.multi-fields', this);
    $('.add-field').click(function() {

        $('.multi-fields').append('<div class="multi-field"><label name="skill"> Skills </label><select name=skills><option></option><option value="UX_Design">UX Design</option> <option value="Transportation_Design">Transportation Design</option><option value="Service_Design">Service Design</option> <option value="Fashion_Design">Fashion Design</option><option value="Graphic_Design">Graphic Design</option><option value="Animation_&amp;_Motion_Design">Animation &amp; Motion Design</option><option value="Typography">Typography</option><option value="Film_&amp;_Advertising">Film &amp; Advertising</option><option value="Design_Research">Design Research</option><option value="Product/Industrial_Design">Product/Industrial Design</option></select><label name="level"> Level' + " " +  '</label><select name=levels><option value= "None">None</option><option value= "Beginner">Beginner</option><option value= "Intermediate">Intermediate</option><option value= "Advanced">Advanced</option></select><a href="#" class="remove_field">Remove</a--></div>');



    });

    $($wrapper).on("click",".remove_field", function(e){ //user click on remove text
			e.preventDefault(); $(this).parent('div').remove(); x--;
		})

});
});


var info = `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>
</head>
<body>

<h2 style="text-align:center">User Profile Card</h2>

<div class="card">
  <img src="/w3images/team2.jpg" alt="John" style="width:100%">
  <h1>John Doe</h1>
  <p class="title">CEO & Founder, Example</p>
  <p>Harvard University</p>
  <div style="margin: 24px 0;">
    <a href="#"><i class="fa fa-dribbble"></i></a>
    <a href="#"><i class="fa fa-twitter"></i></a>
    <a href="#"><i class="fa fa-linkedin"></i></a>
    <a href="#"><i class="fa fa-facebook"></i></a>
  </div>
  <p><button>Contact</button></p>
</div>
`