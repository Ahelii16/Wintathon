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

