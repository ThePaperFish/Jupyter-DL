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

//get all search string location
function getIndicesOf(searchStr, str, caseSensitive) {
    var searchStrLen = searchStr.length;
    if (searchStrLen == 0) {
        return [];
    }
    var startIndex = 0, index, indices = [];
    if (!caseSensitive) {
        str = str.toLowerCase();
        searchStr = searchStr.toLowerCase();
    }
    while ((index = str.indexOf(searchStr, startIndex)) > -1) {
        indices.push(index);
        startIndex = index + searchStrLen;
    }
    return indices;
}

//force download from web
function forceDownload(url, fileName){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.responseType = "blob";
    xhr.onload = function(){
        var urlCreator = window.URL || window.webkitURL;
        var imageUrl = urlCreator.createObjectURL(this.response);
        var tag = document.createElement('a');
        tag.href = imageUrl;
        tag.download = fileName;
        document.body.appendChild(tag);
        tag.click();
        document.body.removeChild(tag);
    }
    xhr.send();
}

//get extension (unknown -> jpg)
function getextension(link){
	var y = getIndicesOf('.',link,false)
	
	var z = [];
	for (var i = 0; i < y.length; i ++) 
	{
		z.push(link.substring(y[i] ,y[i] + 4));
	}
	
	var exts = [".jpg",".png",".gif",".jpe"];
	res = z.filter(f => exts.includes(f));
	if (res[0] == ".jpe")
	{	res[0] = ".jpeg";}
	
	if (res.length > 0)
	{
		return res[res.length - 1];
	}
	else 
	{
		return exts[0];
	}
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
	await sleep(800);
}


// grab the URLs
var urls = $('.rg_di .rg_meta').map(function() { return JSON.parse($(this).text()).ou; });

// // write the URls to file (one per line)
// var textToSave = urls.toArray().join('\n');
// var hiddenElement = document.createElement('a');
// hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave);
// hiddenElement.target = '_blank';
// hiddenElement.download = 'urls.txt';
// hiddenElement.click();

var person = $('input.gLFyf.gsfi')[0].value.replace(/\./g, "");
var tagname = 'Singers_'+ person +'_';

for (var i = 0; i < urls.length; i++)
{
	var target = urls[i];
	if(urls[i].substring(0,5) != "https")
	{ target = urls[i].replace('http','https');}

	forceDownload(target,tagname + i);
	await sleep(500);
	
	if (i % 30 == 0)
	{await sleep(1500);}
}

console.log('complete');
console.log('complete');
console.log('complete');
console.log('complete');
console.log('complete');
console.log('complete');
console.log('complete');


