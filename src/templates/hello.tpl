{% extends "layout.tpl" %}
{% block title %}Hello from Flask{% endblock %}
{% block body %}
{% if name %}
  <h3>Hello {{ name }}!</h3>
{% else %}
  <h1>Hello World!</h1>
{% endif %}

	<p>Using the jQuery load( ) function</p>
	Got this from the server:
	<div id='message'></div>
{% endblock %}

