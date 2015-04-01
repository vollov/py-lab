{% extends "layout.tpl" %}
{% block title %}Index Page {% endblock %}
{% block body %}
<h2>jQuery Example</h2>
<p><input type=text size=5 name=a> +
   <input type=text size=5 name=b> =
   <span id=result>?</span>
<p><a href=# id=calculate>calculate server side</a>
{% endblock %}