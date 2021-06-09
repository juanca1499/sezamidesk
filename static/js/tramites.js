function contarDoc(){
    var docs = document.getElementsByClassName("form-check-input").checkbox;
    var count = 0;

    for(var x=0;x<docs.length;x++){
        if(docs[x].checked){
            count++;
        }
    }
    if(count==docs.length){
        mostrarFormBen();
    }
}

function mostrarFormBen(){
    var seccion_ben = document.getElementById("seccion_beneficiario");
    var parrafos = seccion_ben.getElementsByTagName("p");
    var titulo = parrafos[0].getElementsByTagName("b");
    titulo[0].innerHTML = "Datos del beneficiario"
    parrafos[1].innerHTML = "{{form_beneficiario.as_p}}"
}

function myFunction() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }