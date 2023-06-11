<h1> Mashup Generator </h1>
<h2>1. Description </h2>
A python program to generate mashup of songs of your favourite singer at a single click. It sends the generated file as .zip in your email. <br>

<h2>2. Frameworks and Packages used:  </h2>
For creating mashup : <br>
1. It uses <b>pytube</b> to download videos of singer from youtube. <br>
2. Then, it uses <b>moviepy</b> to convert videos to audio and clips it.<br>
3. Then, using <b> moviepy </b> it merges all the audios.<br>
<br>
For connecting .py file to our frontend : <br>
1. <b>Flask framework</b> is used. It passes requests to web applications.<br>
2. For sending emails, <b>Simple Mail Transfer Protocol(SMTP)</b> is used.<br>
3. email package is used.<br>

<h2>3. How to use:  </h2>
Upon running the app.py file, a link will be generated. Upon clicking, it will lead to the above shown interface.
Upon filling details, and submitting , mashup will be sent to mentioned e-mail, if it exists.


<h2> 1. Screenshot of the interface</h2>
<img src="https://github.com/ankita-1007/Mashup-Generator/assets/100415671/f6e893d5-26bf-48d5-b55c-3b3515b0a81f" width="1000"> <br>







