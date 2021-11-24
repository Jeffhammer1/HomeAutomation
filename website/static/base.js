var data, json, temp, img, data;
var wetterapikey = "fb06a57da86b5439ed6b0b19ff428f0d";

document.onload = requestdata();


/*setInterval(function() {
    requestdata();
}, 10000);*/

function requestdata(a, typ) {
    var request = $.get("/readwetterdata", function(data) {
        if (request.status >= 200 && request.status < 400) {
            if (typ == 1) {
                temp = data.current.temp;
                temp = temp.toFixed(1);
                hum = data.current.humidity;
                hum = hum.toFixed(0);
                wind = data.current.wind_speed
                wind = wind * 3.6
                wind = wind.toFixed(1)
                icon = data.current.weather[0].icon;
                document.getElementById("wetter-temp-jetzt").innerHTML = temp + "C°";
                document.getElementById("wetter-hum-jetzt").innerHTML = hum + "%";
                document.getElementById("wetter-wind-jetzt").innerHTML = wind + "km/h";
                img = "url(http://openweathermap.org/img/wn/" + icon + "@4x.png";
                document.getElementById("wetter-icon").style.backgroundImage = img;

                for (let i = 0; i < a; i++) {
                    z = i;
                    z = z + 1;
                    iconvor = data.daily[i].weather[0].icon;
                    imgvor = "url(http://openweathermap.org/img/wn/" + iconvor + "@4x.png";
                    tmp = data.daily[i].temp.day
                    tmp = tmp.toFixed(1);
                    hum = data.daily[i].humidity;
                    hum = hum.toFixed(0);
                    wind = data.daily[i].wind_speed;
                    wind = wind * 3.6
                    wind = wind.toFixed(1)

                    document.getElementById("wetter-temp-jetzt-d" + z).innerHTML = tmp + "C°";
                    document.getElementById("wetter-hum-jetzt-d" + z).innerHTML = hum + "%";
                    document.getElementById("wetter-wind-jetzt-d" + z).innerHTML = wind + "km/h";
                    document.getElementById("wetter-icon-d" + z).style.backgroundImage = imgvor;
                }
            } else if (typ == 2) {
                temp = data.current.temp;
                temp = temp.toFixed(1);
                hum = data.current.humidity;
                hum = hum.toFixed(0);
                icon = data.current.weather[0].icon;
                document.getElementById("wetter-temp-jetzt").innerHTML = temp + "C°";
                document.getElementById("wetter-hum-jetzt").innerHTML = hum + "%";
                img = "url(http://openweathermap.org/img/wn/" + icon + "@4x.png";
                document.getElementById("wetter-icon").style.backgroundImage = img;
                for (let i = 0; i < a; i++) {
                    z = i;
                    z = z + 1;
                    iconvor = data.daily[i].weather[0].icon;
                    imgvor = "url(http://openweathermap.org/img/wn/" + iconvor + "@4x.png";
                    tmp = data.daily[i].temp.day
                    tmp = tmp.toFixed(1);

                    document.getElementById("wetter-temp-jetzt-d" + z).innerHTML = tmp + "C°";
                    document.getElementById("wetter-icon-d" + z).style.backgroundImage = imgvor;
                }
            }
        } else {
            console.log("error");
        }
    });
}

function requesthuedata() {
    var huedata = $.get("/readhuedata", function(data) {
        if (data.lights[2].state.on == true) {
            console.log(data);

        } else {

        };
    })
};






/*
document.onload = readwetter();

setInterval(function() {
    readwetter();
}, 100000);

function openNav() {
    document.getElementById("sidebar").style.width = "400px";
}

function closeNav() {
    document.getElementById("sidebar").style.width = "0";
}

function AutoRefresh(t) {
    setTimeout("location.reload(true);", t);
}


function readwetter() {
    var request = new XMLHttpRequest;
    request.open("GET", "https://api.openweathermap.org/data/2.5/onecall?lat=47.1921&lon=7.3959&appid=" + wetterapikey + "&units=metric", true);
    request.onload = function() {
        data = JSON.parse(this.response);
        if (request.status >= 200 && request.status < 400) {
            temp = data.current.temp;
            temp = temp.toFixed(1);
            hum = data.current.humidity;
            hum = hum.toFixed(0);
            icon = data.current.weather[0].icon;
            for (let i = 0; i < 4; i++) {
                z = i;
                z = z + 1;
                iconvor = data.daily[i].weather[0].icon;
                imgvor = "url(http://openweathermap.org/img/wn/" + iconvor + "@4x.png";
                tmp = data.daily[i].temp.day
                tmp = tmp.toFixed(1);

                document.getElementById("wetter-temp-jetzt-d" + z).innerHTML = tmp + "C°";
                document.getElementById("wetter-icon-d" + z).style.backgroundImage = imgvor;
            }



            document.getElementById("wetter-temp-jetzt").innerHTML = temp + "C°";
            document.getElementById("wetter-hum-jetzt").innerHTML = hum + "%";
            img = "url(http://openweathermap.org/img/wn/" + icon + "@4x.png";
            document.getElementById("wetter-icon").style.backgroundImage = img;
        } else {
            console.log("error");
        }
    }
    request.send();
}*/