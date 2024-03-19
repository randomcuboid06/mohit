fetch("http://127.0.0.1:5000/")
.then(resp => resp.json())
.then(ans => console.log(ans))