const div = $("DIV#add_item");
div.click(function(){
	$("ul.my_list").append("<li>Item</li>");
});
