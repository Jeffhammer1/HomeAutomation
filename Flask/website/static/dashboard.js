setInterval(function() {
    check_status();
}, 3000);

function check_status() {
    var status = $.get("/status", function(data) {
        console.log(data.status)
        if (data.status == 0) {
            document.getElementById("auto-status").innerHTML = "MAN"
            document.getElementById("auto-status").style.color = "red"
        } else if (data.status == 1) {
            document.getElementById("auto-status").innerHTML = "AUTO"
            document.getElementById("auto-status").style.color = "green"
        }
    })
}

function switch_status() {
    var http = new XMLHttpRequest();
    http.open("POST", "/status", true)
    http.send()
}