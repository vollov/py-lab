<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
    <title>Default Template Page</title>
    <script src="{{url_for('static', filename='jquery-1.7.2.min.js')}}"></script>
	<script type="text/javascript" src="{{url_for('static', filename='my.js')}}"></script>
	<script type=text/javascript>
		$SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
	</script>
	<link rel="stylesheet" type="text/css" href="{{url_for('static', filename='style.css')}}"/>
</head>

<body id="docbody">
<div class=page>
  <h2>This is template page</h2>
  {% block body %}{% endblock %}
</div>
</body>
</html>