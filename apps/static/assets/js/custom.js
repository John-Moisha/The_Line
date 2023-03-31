function USDTcopyToClipboard() {
  var copyText = document.getElementById('USDTValue');
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(copyText.value);
//  alert("Copied the text: " + copyText.value);
}

function BTCcopyToClipboard() {
  var copyText = document.getElementById('BTCValue');
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(copyText.value);
//  alert("Copied the text: " + copyText.value);
}

function ETHcopyToClipboard() {
  var copyText = document.getElementById('ETHValue');
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(copyText.value);
//  alert("Copied the text: " + copyText.value);
}


//$.fn.datepicker.setDefaults({
//    language: 'ru-RU'
//    })
//$('[data-toggle="datepicker"]').datepicker({language: 'ru-RU'});