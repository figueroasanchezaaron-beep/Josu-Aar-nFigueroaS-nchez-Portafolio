// API Key: f853c2ceeb46407dbc1171932221205
// http://api.weatherapi.com/v1/current.json?key=f853c2ceeb46407dbc1171932221205&q=Sahuayo&aqi=no
// fetch(
//   "http://api.weatherapi.com/v1/current.json?key=f853c2ceeb46407dbc1171932221205&q=Sahuayo&aqi=yes"
// )
//   .then((respuesta) => respuesta.json())
//   .then((data) => console.log(data))
//   .catch((error) => console.log(error));

function crear(elemento) {
  return document.createElement(elemento);
}

var regresa = document.querySelector(".regresa");
var resultado = document.querySelector(".resultado");

console.log(regresa);

regresa.onclick = function () {
  window.location = "/";
};

var buscar = document.querySelector(".buscar");

var botonBusqueda = buscar.querySelector("button");
var inputBusqueda = buscar.querySelector("input");
console.log(buscar, botonBusqueda, inputBusqueda);

function buscarCiudad() {
  console.log("Buscar");
  if (inputBusqueda.value == "") return;
  var ciudad = inputBusqueda.value;

  while (resultado.children.length > 0) {
    var temp = resultado.firstChild;
    temp.remove();
  }
  inputBusqueda.value = "";
  var busqueda =
    "http://api.weatherapi.com/v1/current.json?key=f853c2ceeb46407dbc1171932221205&q=" +
    ciudad +
    "&aqi=yes&lang=es";
  fetch(busqueda)
    .then((respuesta) => respuesta.json())
    .then((data) => {
      console.log(data);
      if (typeof data.error != "undefined") crearError();
      else crearCiudad(data);
    })
    .catch((error) => console.log(error));
}

function crearError() {
  var div = crear("div");
  div.classList.add("error");
  div.innerHTML = "La búsqueda no coincide con ningún resultado";
  resultado.append(div);
}

function crearCiudad(ciudad) {
  console.log(ciudad);

  var izquierda = crear("div");
  izquierda.classList.add("izquierda");

  var titulo = crear("div");
  titulo.classList.add("titulo");
  titulo.innerHTML = "El tiempo ahora";

  var actual = crear("div");
  actual.classList.add("actual");
  actual.innerHTML = ciudad.current.last_updated;

  var icono = crear("div");
  icono.classList.add("icono");
  var img = crear("img");
  img.setAttribute("src", ciudad.current.condition.icon);
  icono.append(img);

  var temperaturas = crear("div");
  temperaturas.classList.add("temperaturas");
  temperaturas.innerHTML = ciudad.current.temp_c + "°C";

  var sensacion = crear("div");
  sensacion.classList.add("sensacion");
  sensacion.innerHTML = "Sensación " + ciudad.current.feelslike_c + "°C";

  var condicion = crear("div");
  condicion.classList.add("condicion");
  condicion.innerHTML = "Parcialmente: " + ciudad.current.condition.text;

  var derecha = crear("div");
  derecha.classList.add("derecha");

  var pais_ciudad = crear("div");
  pais_ciudad.classList.add("pais_ciudad");
  pais_ciudad.innerHTML = "Ciudad: " + ciudad.location.name;

  var pais_estado = crear("div");
  pais_estado.classList.add("pais_estado");
  pais_estado.innerHTML = "Estado: " + decode_utf8(ciudad.location.region);

  var pais = crear("div");
  pais.classList.add("pais");
  pais.innerHTML = "País: " + ciudad.location.country;

  var zona_horaria = crear("div");
  zona_horaria.classList.add("zona_horaria");
  zona_horaria.innerHTML = "Zona Horaria: " + ciudad.location.tz_id;

  izquierda.append(titulo);
  izquierda.append(actual);
  izquierda.append(icono);
  izquierda.append(temperaturas);
  izquierda.append(sensacion);
  izquierda.append(condicion);

  derecha.append(pais_ciudad);
  derecha.append(pais_estado);
  derecha.append(pais);
  derecha.append(zona_horaria);

  resultado.append(izquierda);
  resultado.append(derecha);
}

botonBusqueda.onclick = buscarCiudad;

keydown()=crearCiudad;

function decode_utf8(s) {
  return decodeURIComponent(escape(s));
}
