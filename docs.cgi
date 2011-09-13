#!/usr/bin/python

#################################

docpath = "/var/www/html/itensor/docs/"

#################################

import sys

from markdown2 import Markdown
markdowner = Markdown()

import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

def printheader():
    print "Content-Type: text/html\n\n"

md = form.getvalue("value")
page = form.getvalue("page")

if page == None: page = "main"

mdfname = page + ".md"
htfname = page + ".html"

bodyhtml = ""

if md:
    mdfile = open(docpath + mdfname,'w')
    mdfile.write(md)
    mdfile.close()

    bodyhtml = markdowner.convert(md)
    htfile = open(docpath + htfname,'w')
    htfile.write(bodyhtml)
    htfile.close()

    print bodyhtml
    sys.exit(0)

else:
    htfile = open(docpath + htfname,'r')
    bodyhtml = "".join(htfile.readlines())
    htfile.close()

header = \
"""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <title>ITensor - Intelligent Tensor Library</title>
    <meta http-equiv="content-language" content="en" />
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <link rel="icon" href="favicon.ico"/>
    <link rel="stylesheet" href="style.css" type="text/css"/>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.6/jquery.min.js" type="text/javascript"></script>
    <script type="text/javascript">$(document).ready(function(){});</script>
    <script type="text/javascript" src="scripts/jquery.corner.js"></script>
    <script type="text/javascript" src="scripts/jquery.jeditable.mini.js"></script>
    <script type="text/javascript" src="scripts/jquery.autogrow.js"></script>
    <script type="text/javascript" src="scripts/jquery.jeditable.autogrow.js"></script>

    <style type="text/css">

    </style>

</head>

<body>

<div id="main">

<div id="navbar" class="rounded">
    <ul>
    <li><a href="index.html">Home</a> </li>
    <li><a href="news.html">News</a> </li>
    <li><a class="thispage" href="learn.php">Learn</a> </li>
    <li><a href="contribute.html">Contribute</a></li>
    </ul>
</div>


<div id="banner">
<img src="ITensor.png" /></br>
</div>

<div class="full section rounded"> <h2>Documentation</h2> </div>

<div class="full">
<p>
</p>
</div>

<div class="full edit docs" id="input">
"""

footer = \
"""
</div>

<div id="footer"></div>



<script type="text/javascript">
 $(document).ready(function() {
     $('.edit').editable("docs.cgi?page=%s", {
        type : "textarea",
        event : "dblclick",
        onblur : "ignore",
        cancel : "Cancel",
        submit : "OK",
        indicator : 'Saving...',
        loadurl : "docs/main.md"
     });
 });
</script>


</div> <!--class="main"-->

<script type="text/javascript">$(function() {$('.rounded').corner("7px");});</script>

</body>
</html>
""" \
% (page,)

print header
print bodyhtml
print footer
