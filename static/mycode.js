console.log("Javascript loaded");

var searchBox = $("#searchBox");
var query = searchBox.val();

var searchButton = $("#searchButton");
searchButton.click(function(){
    searchBox.val("");
});

