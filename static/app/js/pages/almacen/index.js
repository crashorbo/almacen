const almacenTable = document.querySelector('#datatable-almacen');
const almacenUrl = almacenTable.dataset.url;
const btnAlmacenCreate = document.querySelector('#btn-almacen-create');
const modalContent = document.querySelector('.modal-content');

const almacenes = $('#datatable-almacen').DataTable({
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
    "ajax": almacenUrl
});

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
        almacenes.ajax.reload(null, false);        
    })
}

btnAlmacenCreate.addEventListener('click', (e)=>{
    e.preventDefault();    
    let url = e.target.dataset.url;
    if (!url) {
        url = e.target.parentElement.dataset.url;
    }
    getTemplate(url, modalContent);    
});

modalContent.addEventListener('submit', (e)=> {
    e.preventDefault();
    const url = e.target.getAttribute("action");
    const data = new FormData(e.target);    
    postForm(url, data);
});

almacenTable.addEventListener('click', (e) => {
    if (e.target.classList.contains('fa-trash')) {
        console.log(e.target);
    }    
    if (e.target.classList.contains('fa-edit')) {
        getTemplate(e.target.dataset.url, modalContent);
    }
})