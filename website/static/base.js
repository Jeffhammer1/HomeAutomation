var data, json, temp, img, data;

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