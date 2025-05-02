
document.querySelectorAll(".boton-like").forEach((boton) => {
    boton.addEventListener("click", function () {

        
        const cantidadElemento = this.nextElementSibling.querySelector("#cantidad");

        if (cantidadElemento) {
            
            let cantidad = parseInt(cantidadElemento.textContent.replace(/\D/g, ""), 10);
            cantidad++;
            cantidadElemento.textContent = cantidad; 
        }
    });
});


document.getElementById("form-envio").addEventListener("submit", function(event) {
    document.getElementById("input-url").value = seleccion;
    console.log("Enviado:", seleccion); // Debug
});

