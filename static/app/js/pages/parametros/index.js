const btnCategoriaCreate = document.querySelector('#btn-categoria-create');
const btnUnidadCreate = document.querySelector('#btn-unidad-create');
const modalContent = document.querySelector('.modal-content');
const categoriaTable = document.querySelector('#datatable-categorias');
const categoriaUrl = categoriaTable.dataset.url;
const unidadTable = document.querySelector('#datatable-unidades');
const unidadUrl = unidadTable.dataset.url;

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
        categorias.ajax.reload(null, false);
        unidades.ajax.reload(null, false);
    })
}

btnCategoriaCreate.addEventListener('click', (e)=>{
    e.preventDefault();        
    url = e.target.dataset.url
    if (!url) {
        url = e.target.parentElement.dataset.url;
    }    
    getTemplate(url, modalContent, categorias);
    $('#main-modal').modal('show');
});

btnUnidadCreate.addEventListener('click', (e)=>{
    e.preventDefault();        
    url = e.target.dataset.url
    if (!url) {
        url = e.target.parentElement.dataset.url;
    }    
    getTemplate(url, modalContent);
    $('#main-modal').modal('show');
});

categoriaTable.addEventListener('click', (e) => {
    if (e.target.classList.contains('fa-trash')) {
        console.log(e.target);
    }    
    if (e.target.classList.contains('fa-edit')) {
        getTemplate(e.target.dataset.url, modalContent);
    }
});

unidadTable.addEventListener('click', (e) => {
    if (e.target.classList.contains('fa-trash')) {
        console.log(e.target);
    }    
    if (e.target.classList.contains('fa-edit')) {
        getTemplate(e.target.dataset.url, modalContent);
    }
});

modalContent.addEventListener('submit', (e)=> {
    e.preventDefault();
    const url = e.target.getAttribute("action");
    const data = new FormData(e.target);    
    postForm(url, data);
});