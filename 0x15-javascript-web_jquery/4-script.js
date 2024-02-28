const header = $("header");
const div = $("DIV#toggle_header");
div.click(function(){
	header.toggleClass("green red");
});
