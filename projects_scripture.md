---
layout: default
---
-
<div>
<h1>Random Scripture</h1>

<p>Click the button to trigger a function that will output a random scripture.</p>

<button onclick="retrieveScripture()">Random Scripture</button>

<p id="output"></p>
<script src="scripture.js"></script>

<script>
  function retrieveScripture() {
    document.getElementById("output").innerHTML = getScripture();
  }
</script>
</div>
