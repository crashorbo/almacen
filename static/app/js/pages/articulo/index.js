const articuloUrl = document.querySelector('#page-length-option').dataset.url;
const btnArticuloCreate = document.querySelector('#btn-articulo-create');
const modalContent = document.querySelector('.modal-content');

const articulos = $('#page-length-option').DataTable({
    "language": {
        "decimal":        "",
        "emptyTable":     "No hay datos disponibles en la tabla",
        "info":           "Mostrando _START_ a _END_ de _TOTAL_ entradas",
        "infoEmpty":      "Mostrando 0 a 0 de 0 entradas",
        "infoFiltered":   "(filtered from _MAX_ total entries)",
        "infoPostFix":    "",
        "thousands":      ",",
        "lengthMenu":     "Mostrar _MENU_ entradas",
        "loadingRecords": "Cargando...",
        "processing":     "Procesando...",
        "search":         "Buscar:",
        "zeroRecords":    "No se encontraron registros coincidentes",
        "paginate": {
            "first":      "Primero",
            "last":       "Ultimo",
            "next":       "Siguiente",
            "previous":   "Anterior"
        },
        "aria": {
            "sortAscending":  ": activar para ordenar la columna ascendente",
            "sortDescending": ": activar para ordenar la columna descendente"
        }
    },
    "responsive": true,
    "lengthMenu": [
      [10, 25, 50, -1],
      [10, 25, 50, "All"]
    ],
    "processing": true,
    "serverSide": true,
    "ajax": articuloUrl
});

$(document).ready(() => {
    $('.modal').modal({
        dismissible: false,        
    });    
})

const postData = async (url, data) => {
    await axios(url, {
        method: "POST",
        data: data
    })
    .then(res => {
        if (res.data.status === 200) {
            $('.modal').modal('close');
            categorias.ajax.reload(null, false);
            unidades.ajax.reload(null, false);
            M.toast({
                html: res.data.message,
                classes: "success"
            })          
        } else {
            throw new Error("Error")
        }     
    })
    .catch(error => {
        console.log(error)
    });
}

const getTemplate = async (url, container) => {
    await axios(url)
    .then(res => {
        container.innerHTML = res.data;
        $("#id_unidad").formSelect();          
    });
}

btnArticuloCreate.addEventListener('click', (e)=>{
    e.preventDefault();    
    $('.modal').modal('open');   
    url = btnArticuloCreate.getAttribute('href');
    getTemplate(url, modalContent);
});