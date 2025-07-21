<!DOCTYPE html>
<html class="no-js">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>Tradewind - Ship Generator</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width">

        <link rel="stylesheet" href="static/css/bootstrap.min.css">
        <link rel="stylesheet" href="static/css/main.css">
        <!-- Dark mode stylesheet (disabled by default) -->
        <link id="dark-css" rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootswatch/3.4.1/darkly/bootstrap.min.css" disabled>
        
        <script src="static/js/vendor/modernizr-2.6.2.min.js"></script>
    </head>
    <body>
        <!-- Theme toggle button -->
        <button id="theme-toggle" class="btn btn-default" style="position: fixed; top: 1rem; right: 1rem; z-index: 1050;">🌙</button>
        {% include 'ship.tpl' with context %}

<!--         {# include 'sidebar.tpl' with context #} -->
        
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
        <script>window.jQuery || document.write('<script src="static/js/vendor/jquery-1.10.2.min.js"><\/script>')</script>
        <script src="static/js/vendor/bootstrap.min.js"></script>
        <script src="static/js/main.js"></script>
    </body>
</html>
