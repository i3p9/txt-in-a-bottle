function toClipboard(){
    var copyText = document.getElementById("shareLink");
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
    var endPoint = copyText.value;
    endPoint = "https://txtinabottle.herokuapp.com" + endPoint
    console.log(endPoint)
    navigator.clipboard.writeText(endPoint);
    console.log("Copied to clipboard");
    // document.getElementById("clipboardMessage").style.display = "inline";
    // setTimeout(() => {document.getElementById("clipboardMessage").style.display = "none"}, 1000);
}

function openInNewTab() {
    var copyText = document.getElementById("shareLink");
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
    var endPoint = copyText.value;
    newURL = "https://txtinabottle.herokuapp.com" + endPoint + "raw"
    console.log(newURL)
    window.open(newURL, '_blank').focus();
}

function createWebpage() {
    var copyText = document.getElementById("shareLink");
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
    var endPoint = copyText.value;
    newURL = "https://txtinabottle.herokuapp.com" + endPoint + "page"
    console.log(newURL)
    window.open(newURL, '_blank').focus();
}

function showCreateUI(){
    document.getElementById('homepageui').style.display="none";
    document.getElementById('createui').style.display="block";
    document.getElementById('txtareainput').focus();

}

function showHomeUI(){
    document.getElementById('homepageui').style.display="block";
    document.getElementById('createui').style.display="none";

}
