// pull down jquery into the JavaScript console
var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script);

//pull down the windows
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

//scroll bottom
function scrollbottom(){
	window.scrollTo(0,document.body.scrollHeight);
}

//click more images
function clickmore(){
	var x = document.querySelectorAll("#smbw .ksb");
	x[0].click();
}

var i,x,y;
var interval = 800;

for (y = 0; y < 2; y ++)
{
	for (x = 0; x < 4; x ++)
	{
		window.setTimeout(scrollbottom(), i);
		await sleep(1000);
	}
	window.setTimeout(clickmore(), i);
	await sleep(1500);
}


// grab the URLs
var urls = $('.rg_di .rg_meta').map(function() { return JSON.parse($(this).text()).ou; });

var person = $('input.gLFyf.gsfi')[0].value.replace(/\./g, "");

// write the URls to file (one per line)
var textToSave = urls.toArray().join('\n');
var hiddenElement = document.createElement('a');
hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave);
hiddenElement.target = '_blank';
hiddenElement.download = person + '.txt';
hiddenElement.click();



