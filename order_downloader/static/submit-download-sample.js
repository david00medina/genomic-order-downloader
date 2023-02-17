var form = document.getElementById("download-sample-form");
form.onsubmit = function (event) {
  var xhr = new XMLHttpRequest();
  var formData = new FormData(form);
  xhr.open('POST', 'http://localhost:8000/api/download-sample');
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify(Object.fromEntries(formData)));
  xhr.onreadystatechange = function () {
    if (xhr.readyState == XMLHttpRequest.DONE) {
      form.reset();
    }
  }
  return false;
}