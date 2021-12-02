const btnCategoriaCreate = document.querySelector('#btn-categoria-create');
const btnUnidadCreate = document.querySelector('#btn-unidad-create');
const modalContent = document.querySelector('.modal-content');
const categoriaUrl = document.querySelector('#datatable-categorias').dataset.url;
const unidadUrl = document.querySelector('#datatable-unidades').dataset.url;

const categorias = $('#datatable-categorias').DataTable({
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
    "ajax": categoriaUrl
});

const unidades = $('#datatable-unidades').DataTable({
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
    "ajax": unidadUrl
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
    });
}

btnCategoriaCreate.addEventListener('click', (e)=>{
    e.preventDefault();
    $('.modal').modal('open');
    url = btnCategoriaCreate.getAttribute('href');
    getTemplate(url, modalContent);
});

btnUnidadCreate.addEventListener('click', (e)=>{
    e.preventDefault();
    $('.modal').modal('open');
    url = btnUnidadCreate.getAttribute('href');
    getTemplate(url, modalContent);
});

modalContent.addEventListener('submit', (e)=> {
    e.preventDefault();
    const url = e.target.getAttribute("action");
    const data = new FormData(e.target);    
    postData(url, data)
})