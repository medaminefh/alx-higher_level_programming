const header = $("header");
const div = $("DIV#red_header");
div.click(function(){
	header.toggleClass("green red");
});
