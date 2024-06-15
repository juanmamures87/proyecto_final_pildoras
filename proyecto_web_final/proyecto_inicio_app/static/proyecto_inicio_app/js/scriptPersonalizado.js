/**
 * Código para conseguir que los nombres indicadores de página del navbar aparezcan seleccionados
 */

// Obtiene todos los elementos 'nav-item'
let navItems = document.querySelectorAll(".nav-item");

// Elimina la clase 'active' de todos los elementos 'nav-item'
navItems.forEach(function (navItem) {
  navItem.classList.remove("active");
});

// Obtiene la ruta de la URL actual
let rutaActual = window.location.pathname;

// Añade la clase 'active' al elemento 'nav-item' que corresponde a la URL actual
navItems.forEach(function (navItem) {
  let anchor = navItem.querySelector("a");
  if (anchor.getAttribute("href") === rutaActual) {
    navItem.classList.add("active");
  }
});

////////////////////////////////////////////////////////////////////////////////////////////////