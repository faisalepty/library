const bookModal = document.getElementById('myModal');
const addBookFormBtn = document.getElementById('addbook');
const navAddBookBtn = document.getElementsByClassName('addBookBtn')[0];

const resetInputs = () => {
  const inputNames = ['title', 'author', 'description', 'language', 'category', 'edition', 'pages', 'publisher', 'publish_date', 'img_url', 'quantity', 'fee'];
  inputNames.forEach(name => {
    const input = document.getElementsByName(name)[0];
    input.value = '';
  });
};



navAddBookBtn.addEventListener('click', () => {
  addBookFormBtn.classList.remove('d-none');
  const updateBtn = document.getElementById('updatebtn');
  updateBtn.style.display = 'none';
  const title = bookModal.getElementsByClassName('modal-title')[0].firstChild
    title.innerText = 'ADD BOOK'
  resetInputs();
});

addBookFormBtn.addEventListener('click', (e) => {
  e.preventDefault();
  const csrfTokenInput = document.getElementById('csrf_token').firstChild;
  const inputNames = ['title', 'author', 'description', 'language', 'category', 'edition', 'pages', 'publisher', 'publish_date', 'img_url', 'quantity', 'fee'];

  const datar = inputNames.reduce((data, name) => {
    data[name] = document.getElementsByName(name)[0].value;
    return data;
  }, {
    status: 'On shelf',
    csrfmiddlewaretoken: csrfTokenInput.value
  });
console.log(datar)
  $.ajax({
    type: 'POST',
    url: '/newbook/',
    headers: { 'X-Requested-With': 'XMLHttpRequest' },
    data: datar,
    success: (res) => {

      resetInputs();
      bookModal.classList.remove('show');
      bookModal.style.display = 'none';
      if (res.success){
        successAlert(res.success);
      }else if(res.error){
        bookModal.classList.remove('show');
        bookModal.style.display = 'none';
        errorAlert(res.error)
      }
      
    },
    error: (res) => {
      bookModal.classList.remove('show');
        bookModal.style.display = 'none';
    }
  });
});
