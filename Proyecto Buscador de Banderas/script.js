var buscar = document.querySelector(".buscar");
var botonBusqueda = buscar.querySelector("button");
var inputBusqueda = buscar.querySelector("input");
var regresa = document.querySelector(".regresa");
var resultado = document.querySelector(".resultado");
console.log(buscar, botonBusqueda, inputBusqueda, resultado, regresa);

function Crear(elemento) {
  return document.createElement(elemento);
}

function crearContacto(contacto) {
  console.log(contacto);
  var div = Crear("div");
  div.classList.add("contacto");

  var foto = Crear("div");
  foto.classList.add("foto");
  var img = Crear("img");
  img.setAttribute("src", contacto.flags.png);
  img.onclick = traerModal;
  foto.append(img);

  var info = Crear("div");
  info.classList.add("info");

  var nombre = Crear("div");
  nombre.classList.add("nombre");
  nombre.innerHTML = contacto.name;

  var code = Crear("div");
  code.classList.add("cod");
  code.innerHTML = contacto.alpha2Code;

  info.append(nombre);
  info.append(code);

  div.append(foto);
  div.append(info);

  resultado.append(div);
}

function buscarCiudad() {
  console.log("buscar");
  if (inputBusqueda.value == "") return;
  var ciudad = inputBusqueda.value;

  while (resultado.children.length > 0) {
    var temp = resultado.firstChild;
    temp.remove();
  }
  inputBusqueda.value = "";

  var busqueda = "https://restcountries.com/v2/name/" + ciudad;
  fetch(busqueda)
    .then((respuesta) => respuesta.json())
    .then((data) => {
      console.log(data);

      for (x = 0; x < data.length; x++) {
        var contacto = data[x];
        console.log("Entrar");
        crearContacto(contacto);
      }
    });
}
botonBusqueda.onclick = buscarCiudad;
var modal = document.querySelector(".modal");

var comp = 0;

function traerModal(e) {
  if (comp != 0) {
    document.querySelector(".tarjeta").remove();
  }

  comp = 1;
  var modal = document.querySelector(".modal");
  console.log(modal);
  modal.removeChild;
  var padre = e.target.parentNode.parentNode.parentNode;
  console.log(padre);
  var link = padre.querySelector(".info");
  link = link.querySelector(".cod");
  link = link.innerHTML;

  console.log(link);

  var busqueda = "https://restcountries.com/v2/alpha/" + link;

  fetch(busqueda)
    .then((respuesta) => respuesta.json())
    .then((data) => {
      console.log(data);

      modal.style.display = "flex";
      var tarjeta = Crear("div");
      tarjeta.classList.add("tarjeta");

      var bandera = Crear("div");
      bandera.classList.add("bandera");

      var img = Crear("img");
      img.setAttribute("src", data.flags.png);
      bandera.append(img);
      console.log(bandera);

      document.getElementById("modal").style.backgroundImage = img;

      var pais = Crear("div");
      pais.classList.add("pais");
      pais.innerHTML = data.nativeName;
      console.log(pais);

      if (pais.innerHTML == "Antarctica") {
        var code = Crear("div");
        code.classList.add("uno");
        code.innerHTML = data.alpha2Code;

        var llamada = Crear("div");
        llamada.classList.add("dos");
        llamada.innerHTML = "+" + data.callingCodes;

        var region = Crear("div");
        region.classList.add("tres");
        region.innerHTML = data.region;

        var poblacion = Crear("div");
        poblacion.classList.add("cuatro");
        poblacion.innerHTML = data.population;

        var lenguaje = Crear("div");
        lenguaje.classList.add("cinco");
        lenguaje.innerHTML = data.languages[0].nativeName;

        var informa = Crear("div");
        informa.classList.add("informa");
        var texto = Crear("div");
        texto.innerHTML = "Acerca de:";
        texto.setAttribute("id", "texto");

        informa.append(texto, code, llamada, region, poblacion, lenguaje);

        tarjeta.append(bandera, pais, informa);
      } else {
        var n = Crear("div");
        n.classList.add("n");
        n.innerHTML = "País: " + data.name;

        var code = Crear("div");
        code.classList.add("code");
        code.innerHTML = "Código: " + data.alpha2Code + " / " + data.alpha3Code;

        var llamada = Crear("div");
        llamada.classList.add("llamada");
        llamada.innerHTML = "Prefijo telefónico: +" + data.callingCodes;

        var capital = Crear("div");
        capital.classList.add("capital");
        capital.innerHTML = "Capital: " + data.capital;

        var region = Crear("div");
        region.classList.add("region");
        region.innerHTML = "Continente:" + data.region;

        var gentilisio = Crear("div");
        gentilisio.classList.add("altSpelling1");
        gentilisio.innerHTML = "Gentilisio: " + data.demonym;

        var poblacion = Crear("div");
        poblacion.classList.add("poblacion");
        poblacion.innerHTML = "Población: " + data.population;
        var moneda = Crear("div");
        moneda.classList.add("moneda");
        moneda.innerHTML = "Moneda: " + data.currencies[0].name;

        var lenguaje = Crear("div");
        lenguaje.classList.add("lenguaje");
        lenguaje.innerHTML = "Idioma: " + data.languages[0].nativeName;

        var simbolo = Crear("div");
        simbolo.classList.add("simbolo");
        simbolo.innerHTML = "Símbolo: " + data.currencies[0].symbol;

        var area = Crear("div");
        area.classList.add("area");
        area.innerHTML = "Área: " + data.area + " cm²";

        var horario = Crear("div");
        horario.classList.add("horario");
        horario.innerHTML = data.timezones;
        console.log(horario);

        var informa = Crear("div");
        informa.classList.add("informa");
        var texto = Crear("div");
        texto.innerHTML = "Acerca de:";
        texto.setAttribute("id", "texto");

        informa.append(
          texto,
          n,
          moneda,
          simbolo,
          lenguaje,
          area,
          code,
          llamada,
          capital,
          region,
          gentilisio,
          poblacion
        );

        tarjeta.append(bandera, pais, informa);
      }
      modal.append(tarjeta);
      console.log(tarjeta);
    });
}

modal.onclick = function () {
  modal.style.display = "none";
  document.querySelector(".tarjeta").remove();
  comp = 0;
};

function decode_utf8(s) {
  return decodeURIComponent(escape(s));
}
