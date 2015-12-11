console.log("Javascript loaded");

var searchIDButton = $("#searchIDButton");
searchIDButton.click(function(){
    var searchIDBox = $("#searchIDBox");
    var IDQuery = searchIDBox.val();
    searchIDBox.val("");
    $.getJSON("/searchbyid",{searchIDBox:IDQuery},function(IDQuery){
	// empties the list so it only displays the Pokemon in the current search
	console.log(IDQuery);
	$("#resultList").empty();
	$("#resultList").append($("<li id='name0'>Name : "+IDQuery.name+"</li>"));
    });
});

var searchNameButton = $("#searchNameButton");
searchNameButton.click(function(){
    var searchNameBox = $("#searchNameBox");
    var NameQuery = searchNameBox.val();
    searchNameBox.val("");
    $.getJSON("/searchbyname",{searchNameBox:NameQuery},function(NameQuery){
	// empties the list so it only displays the Pokemon in the current search
	$("#resultList").empty();
	console.log(NameQuery);
	keys = Object.keys(NameQuery);
	console.log(keys);
	length = keys.length;
	console.log(length);
	for (i=0; i<length; i++){
	    console.log(NameQuery[keys[i]]);
	    $("#resultList").append($("<li id='name"+i+"'>Name : "+NameQuery[keys[i]].name+"</li>"));
	};
    });
});

