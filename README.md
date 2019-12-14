# project99
A note-taking, question anonymised question asking web framework for Teachers and students.

##Requirements and dependencies
Requires Python3.8, the websockets python library (`pip install websockets`)

This application utilises bulma.io for CSS styles, and the trumbowyg library for the text editor.

Run the websocket server with `python websocketserver2.py`, change the url in classroom.html to your domain. Note that some web browsers (only Firefox being the major browser which does this at time of writing) autorejects connections without an SSL certificate, which can be temporarily disable through the `about:config` page by toggling the `network.websocket.allowInsecureFromHTTPS` parameter to false.

The default passwords for the teacher is `12345` and the default password for the monitor is `54321`. For the monitor to approve a question, click on the question.
