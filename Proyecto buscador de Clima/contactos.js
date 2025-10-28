var contactos = document.querySelector(".contactos");
console.log(contactos);

function crear(elemento) {
  return document.createElement(elemento);
}

function crearContacto(contacto) {
  // console.log(contacto);
  var div = crear("div");
  div.classList.add("contacto");

  var foto = crear("div");
  foto.classList.add("foto");

  var img = crear("img");
  img.setAttribute("src", contacto.avatar);
  foto.append(img);

  var info = crear("div");
  info.classList.add("info");

  var id = crear("div");
  id.classList.add("id");
  id.innerHTML = contacto.id;

  var nombre = crear("div");
  nombre.classList.add("nombre");
  nombre.innerHTML = contacto.name;

  var tele = crear("div");
  tele.classList.add("tele");
  tele.innerHTML = contacto.tel;

  info.append(id);
  info.append(nombre);
  info.append(tele);

  div.append(foto);
  div.append(info);
  contactos.append(div);
}

fetch("https://62796baf73bad50685784ba6.mockapi.io/api/v1/contactos")
  .then((respuesta) => respuesta.json())
  .then((data) => {
    // console.log(data);
    for (x = 0; x < data.length; x++) {
      var contacto = data[x];
      crearContacto(contacto);
    }
  });

var regresa = document.querySelector(".regresa");
console.log(regresa);
regresa.onclick = function () {
  window.location = "/";
};
