---
layout: noheader
---


I am a writer, designer, free thinker.
My focus is creation.


{% include projects-list.md %}

<br>

<form id="my-form" action="https://formspree.io/xzbjybrn" method="POST">
<h1 style="font-size: 36px;"> Looking to Connect? </h1><br>
<label>Name:</label>
  <input type="text" name="name" placeholder="your name">
  <label>Email:</label>
  <input type="email" name="email" placeholder="your email"/>         <br>
  <label>Message:</label>
  <input type="text" name="message" placeholder="your message"/>
  <button id="my-form-button">Send</button>
  <p id="my-form-status"></p>
</form>
You can also find me on [Facebook](https://www.facebook.com/james.bytes.73).


<script>
  window.addEventListener("DOMContentLoaded", function() {

    // get the form elements defined in your form HTML above

    var form = document.getElementById("my-form");
    var button = document.getElementById("my-form-button");
    var status = document.getElementById("my-form-status");

    // Success and Error functions for after the form is submitted

    function success() {
      form.reset();
      button.style = "display: none ";
      status.innerHTML = "Thanks, I will get back with you soon! -JB";
    }

    function error() {
      status.innerHTML = " There was a problem. :( :( :( Try refreshing the page?";
    }

    // handle the form submission event

    form.addEventListener("submit", function(ev) {
      ev.preventDefault();
      var data = new FormData(form);
      ajax(form.method, form.action, data, success, error);
    });
  });

  // helper function for sending an AJAX request

  function ajax(method, url, data, success, error) {
    var xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.setRequestHeader("Accept", "application/json");
    xhr.onreadystatechange = function() {
      if (xhr.readyState !== XMLHttpRequest.DONE) return;
      if (xhr.status === 200) {
        success(xhr.response, xhr.responseType);
      } else {
        error(xhr.status, xhr.response, xhr.responseType);
      }
    };
    xhr.send(data);
  }
</script>
