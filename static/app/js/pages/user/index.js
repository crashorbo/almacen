const datatableUsuario = document.querySelector("#datatable-usuario");
const btnUsuario = document.querySelector("#btn-usuario");
const modalContent = document.querySelector(".modal-content");
$("#datatable-usuario").DataTable({
    "responsive": true,
    "lengthMenu": [
      [10, 25, 50, -1],
      [10, 25, 50, "All"]
    ],
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
        $('#main-modal').modal('hide')
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