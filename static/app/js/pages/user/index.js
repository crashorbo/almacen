const datatableUsuario = document.querySelector("#datatable-usuario");
const btnUsuario = document.querySelector("#btn-usuario");
const modalContent = document.querySelector(".modal-content");
const tablaUsuario = document.querySelector('#datatable-usuario');
const usuarioUrl = tablaUsuario.dataset.url;
const tableUsuario = $("#datatable-usuario").DataTable({
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
    "columnDefs": [ {
        "targets": [7],
        "orderable": false
    }],
    "responsive": true,
    "lengthMenu": [
      [10, 25, 50, -1],
      [10, 25, 50, "All"]
    ],
    "processing": true,
    "serverSide": true,
    "ajax": usuarioUrl
})

const getTemplate = async(url, container) => {    
    await axios(url)
    .then( res => {
        container.innerHTML = res.data;
        $('#main-modal').modal('show');
    })
}

const postForm = async(url, data) => {
    await axios(url, {
        method: 'post',
        data: data
    })
    .then( res => {
        console.log(res.data);
        $('#main-modal').modal('hide');
        tableUsuario.ajax.reload(null, false);
    })
}

btnUsuario.addEventListener('click', (e) => {
    e.preventDefault();
    let url = e.target.dataset.url;
    if (!url) {
       url = e.target.parentElement.dataset.url;
    }
    getTemplate(url, modalContent);
})

modalContent.addEventListener("submit", (e) => {
    e.preventDefault();
    postForm(e.target.getAttribute("action"), new FormData(e.target));
})

tablaUsuario.addEventListener('click', (e) => {
    if (e.target.classList.contains('fa-trash')) {
        console.log(e.target);
    }    
    if (e.target.classList.contains('fa-edit')) {
        getTemplate(e.target.dataset.url, modalContent);
    }    
})