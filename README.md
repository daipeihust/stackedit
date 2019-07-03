```
<!DOCTYPE html>
<html lang="en">
   <head>
	 <script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/8.0.0/mermaid.min.js"></script>
    </head>
	 
<body>
 <pre><code class="language-mermaid">graph LR
A--&gt;B
</code></pre>

<div class="mermaid">graph LR
A--&gt;B
</div>
	
</body>
<script>
var config = {
    startOnLoad:true,
    theme: 'forest',
    flowchart:{
            useMaxWidth:false,
            htmlLabels:true
        }
};
mermaid.initialize(config);
window.mermaid.init(undefined, document.querySelectorAll('.language-mermaid'));
</script>

</html>
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgxMTM5NDQ1MSwxNDI1MDUyODg1LDczOD
k3Mjg3LDE4OTkyODczMDYsLTg3NzAxNjUyNCw1MTAyOTEzMDIs
LTg1NTY3MTU0NywzMjIxOTI0ODcsLTIwODg3NDY2MTIsLTE2MD
I0NDEwMyw5MzcyODk3LC0xMzY3ODMyMzE1LDc3NzMyNTYzMSw2
MzcwMjY5NjcsMTgzNTQxNjIzMywtODcxNjE5MDM2XX0=
-->