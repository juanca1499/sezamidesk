function muestraModal(url){
    document.getElementById('formEliminar').action = url;
    document.getElementById('modalCuerpo').innerHTML = 
    `¿Está seguro que desea eliminar el registro?`;
}