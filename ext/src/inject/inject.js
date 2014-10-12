chrome.extension.sendMessage({}, function(response) {

		console.log('fffff');

	var readyStateCheckInterval = setInterval(function() {
	if (document.readyState === "complete") {
		clearInterval(readyStateCheckInterval);

		// ----------------------------------------------------------
		// This part of the script triggers when page is done loading
		console.log("Hello. This message was sent from scripts/inject.js");
		// ----------------------------------------------------------

		// Get side panel image
		var img = document.querySelector(".infobox.vcard").querySelector("img");
		img.src = '//127.0.0.1:5000/'+img.src;


	}
	}, 10);
});
