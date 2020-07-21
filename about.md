---
layout: default
---

I am a writer, designer, free thinker.
My focus is creation.

<form id="my-form" action="https://formspree.io/xzbjybrn" method="POST">
<h1> Contact Me </h1><br>
<label>Name:</label>
  <input type="text" name="name" placeholder="your name">
  <label>Email:</label>
  <input type="email" name="email" placeholder="your email"/>         <br>
  <label>Message:</label>
  <input type="text" name="message" placeholder="your message"/>
  <button id="my-form-button">Send</button>
  <p id="my-form-status"></p>
</form>
You can also find me on find me on [Facebook](https://www.facebook.com/james.bytes.73).

<!--
I am a writer, coder, web designer, free thinker.

You can connect with me at JamesBytes1@gmail.com and  -->

<br>
# My Mission:

I aim **to create systems of interactive text-based therapeutic resources** available for all to use freely. <!-- (_optimally while disrupting the established powers that be_).-->


# But. What does that mean?

That means I want to create programs that change people's perspectives about life, what matters, and eventually to help them work through trauma.


# My plan:

I am starting with small projects and working my way up from there. I started with text-based motivational bots as a small hobby. I'm now designing [a program](/thedecisionmaker.html)
that walks individuals through making life decisions, their goals, and their calling in life.

<br>

# And just what exactly do I aim to build one day?

I will build programs of increasing scope. I plan to take the experience gained along the way to create an intelligence that capable of providing extensive therapy to anyone, perhaps with much more complex work like grief.

# Basically,

#### I want to take code like this:

```python
   print "What do you mean I'm actually code?"
   print "You want me to help people?"
   if True:
      print "I can't do that!"
```

#### and turn it into this.

```
Nancy Drew,
Let's talk through some of your trauma today.
```

# And well,

I want it to be free.
Like. All the time free.
Not like, _monthly subscription_ "free" or _if you can afford insurance_ "free",
like free free. For ev-er-ey-bo-dy. For like, ever.

# And. And. And.

and I want to see what grows and where this goes. Because I care about this. And I think it's worth caring about.

And I know it's possible, and I know this will come into the world with or without me.

# If you'd consider supporting my projects and vision on Patreon..

## [Take the Red Pill](https://patreon.com/motibytes) or [Take the Red Pill](https://patreon.com/motibytes).
<br>
<br>
<br>
<br>

<!--
<form action="https://formspree.io/xzbjybrn" method="POST">
  Name: <input type="text" name="name" placeholder="Your name">
  Email: <input type="email" name="_replyto" placeholder="Your email">
  Message: <textarea name="message" placeholder="Type Your Message"></textarea>
  <input type="submit" value="Send">
</form>
-->
<!-- modify this form HTML and place wherever you want your form -->


<!-- Place this script at the end of the body tag -->

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
      status.innerHTML = "Thanks, I will get back with you soon!";
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

<!--## FAQ

<!--
<dl>
<dt>I don't really get it?</dt>
<dd>I don't expect everyone or even anyone to see my vision. I feel this is calling me. I'm going for it. </dd>
<dt>I have questions.</dt>
<dd>You can always shoot me an email at jamesbytes1@gmail.com</dd>



-->
<!--
hey future me, am i looking for the original article? theres a bak file.
# My motivation:

Really I just want to influence people's lives for the better.

To give people a brighter perspective about life.

And, ideally, to survive while doing so.

( Even more ideally, to mass distribute the most beneficial of the _dominant-American-Psychology-monopoly-name-I-can't-say-here_'s
methods for free, because I find it ethically correct to do so)


# What will I need?

Time. ~~It takes 10,000 hours to master a craft.
Which means I'll need about
10,000 hours total at 10 hours per day is 1000 days, 5 days of the week is 1,400 days, which equates to 3.845 years or just about 4 years and several projects later~~. A lot of time.
I'll need the time to build these projects, and a vast amount of time to
gather existing therapy resources. I need funding to make it through that time.
-->
<!--
I am an _excellent_ independent researcher, and can gain any required skills
and information along the way. -->
<!--
I don't want to spend _some_ of my free time doing this,
_-as I was before, dedicating nearly every spare moment I had to this-_
I want to spend _**all**_ of my working hours doing this,
for the rest of my life, and see what grows and where it goes.
Because I care about this. And I think it's worth caring about.
And I know it's possible, and I know it will happen one way or another.

# And. And. And.

I want it to be free.
Like. All the time free.
Not like, _monthly subscription_ "free" or _if you can afford insurance_ "free",
like free free. For ev-er-ey-bo-dy. For like, ever.
-->
