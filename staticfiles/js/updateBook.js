const updateBookModal = document.getElementById('myModal')
const updateBookBtn = document.getElementsByClassName('updateBookBtn')
const buttonsArr = [...updateBookBtn]
let status
buttonsArr.forEach(btn => {
  btn.addEventListener('click', (e) =>{
    id = e.target.id
  $.ajax({
    type:'GET',
    url: `/editbookinfo/${id}`,
    success: (res) => {
      const titleInput = document.getElementsByName('title')[0];
    const authorInput = document.getElementsByName('author')[0];
    const descriptionInput = document.getElementsByName('description')[0];
    const languageInput = document.getElementsByName('language')[0];
    const categoryInput = document.getElementsByName('category')[0];
    const editionInput = document.getElementsByName('edition')[0];
    const pagesInput = document.getElementsByName('pages')[0];
    const publisherInput = document.getElementsByName('publisher')[0];
    const publishDateInput = document.getElementsByName('publish_date')[0];
    const imgUrlInput = document.getElementsByName('img_url')[0];
    const quantityInput = document.getElementsByName('quantity')[0];
    const feeInput = document.getElementsByName('fee')[0];
    status = res.data.status

    titleInput.value = `${res.data.title}`;
            authorInput.value = `${res.data.author}`;
            descriptionInput.value = `${res.data.description}`;
            languageInput.value = `${res.data.language}`;
            categoryInput.value = `${res.data.category}`;
            editionInput.value = `${res.data.edition}`;
            pagesInput.value = `${res.data.pages}`;
            publisherInput.value = `${res.data.publisher}`;
            publishDateInput.value = `${res.data.publish_date}`;
            imgUrlInput.value = `${res.data.img_url}`;
            quantityInput.value = `${res.data.quantity}`;
            feeInput.value = `${res.data.fee}`;
    addBookFormBtn.classList.add('d-none')
    const updateBtn = document.getElementById('updatebtn') 
    updateBtn.style.display = 'block'
    const title = updateBookModal.getElementsByClassName('modal-title')[0].firstChild
    title.innerText = 'UPDATE BOOK'
    }

  })
  })
})


const updateBtn = document.getElementById('updatebtn')

updateBtn.addEventListener('click', (e) => {
  const titleInput = document.getElementsByName('title')[0];
    const authorInput = document.getElementsByName('author')[0];
    const descriptionInput = document.getElementsByName('description')[0];
    const languageInput = document.getElementsByName('language')[0];
    const categoryInput = document.getElementsByName('category')[0];
    const editionInput = document.getElementsByName('edition')[0];
    const pagesInput = document.getElementsByName('pages')[0];
    const publisherInput = document.getElementsByName('publisher')[0];
    const publishDateInput = document.getElementsByName('publish_date')[0];
    const imgUrlInput = document.getElementsByName('img_url')[0];
    const quantityInput = document.getElementsByName('quantity')[0];
    const feeInput = document.getElementsByName('fee')[0]; 
    const csrfTokenInput = document.getElementById('csrf_token').firstChild;
  

    const datar = {
        'title': titleInput.value,
        'author': authorInput.value,
        'description': descriptionInput.value,
        'language': languageInput.value,
        'category': categoryInput.value,
        'edition': editionInput.value,
        'pages': pagesInput.value,
        'publisher': publisherInput.value,
        'publish_date': publishDateInput.value,
        'img_url': imgUrlInput.value,
        'quantity': quantityInput.value,
        'fee': feeInput.value,
        'status': status,
        'csrfmiddlewaretoken': csrfTokenInput.value
    };
      $.ajax({
        type: 'POST',
        url: `/editbookinfo/${id}`,
        headers: {'X-Requested-With': 'XMLHttpRequest'
      },
        data: datar,
        success: (res) => {
          if(res.success){
          const inputs = Object.values(datar)
          titleInput.value = '';
            authorInput.value = '';
            descriptionInput.value = '';
            languageInput.value = '';
            categoryInput.value = '';
            editionInput.value = '';
            pagesInput.value = '';
            publisherInput.value = '';
            publishDateInput.value = '';
            imgUrlInput.value = '';
            quantityInput.value = '';
            feeInput.value = '';
            updateBookModal.classList.remove('show')
            updateBookModal.style.display = 'none'
            successAlert()}else if(res.error){
              errorAlert(res.error)
            }
        },
        error: (res) => {
          errorAlert(res.error)
        }

      })
})

