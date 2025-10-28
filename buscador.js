var paises = document.querySelector(".paises");
console.log(paises);
var tarjeta = document.querySelector(".tarjeta");

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

function buscarPais() {
  console.log("Buscar");
  if (inputBusqueda.value == "") return;
  var pas = inputBusqueda.value;
  inputBusqueda.value = "";
  var busqueda = "https://restcountries.com/v2/name/" + pas;
  console.log(busqueda);

  while (resultado.children.length > 0) {
    var temp = resultado.firstChild;
    temp.remove();
  }

  fetch(busqueda)
    .then((respuesta) => respuesta.json())
    .then((data) => {
      console.log(data);
      if (typeof data.error != "undefined") crearError();
      else {
        // console.log(data);
        for (x = 0; x < data.length; x++) {
          var pais1 = data[x];
          crearPais(pais1);
        }
      }
    })
    .catch((error) => console.log(error));
}

function crearError() {
  var div = crear("div");
  div.classList.add("error");
  div.innerHTML = "La búsqueda no coincide con ningún resultado";
  resultado.append(div);
}
var icono = crear("div");
icono.classList.add("icono");
var img = crear("img");

function crearPais(pais) {
  var izquierda = crear("div");
  izquierda.classList.add("izquierda");

  // var icono = crear("div");
  // icono.classList.add("icono");
  // var img = crear("img");

  img.setAttribute("src", pais.flags.png);
  icono.append(img);

  var derecha = crear("div");
  derecha.classList.add("derecha");

  var nombre = crear("div");
  nombre.classList.add("pais_ciudad");
  nombre.innerHTML = "Pais: " + pais.name;

  var code = crear("div");
  code.classList.add("pais_estado");
  code.innerHTML = "Código: " + pais.alpha2Code;

  var capital1 = crear("div");
  capital1.classList.add("pais");
  capital1.innerHTML = "Capital: " + pais.capital;

  izquierda.append(icono);
  derecha.append(nombre);
  derecha.append(code);
  derecha.append(capital1);

  resultado.append(derecha);
  resultado.append(izquierda);
  // paises.append(div);
}

var modal = document.querySelector(".modal");

icono.onclick = function (pais1) {
  modal.style.display = "flex";
  // if()
  //   var img = crear("div");
  //   img.setAttribute("src", pais1.flags.png);

  //   tarjeta.append(img);
};
modal.onclick = function () {
  modal.style.display = "none";
};

botonBusqueda.onclick = buscarPais;

function decode_utf8(s) {
  return decodeURIComponent(escape(s));
}
