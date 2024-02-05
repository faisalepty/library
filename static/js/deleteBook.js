const deleteBookBtns = document.getElementsByClassName('deleteBookBtn');
const deleteBookModal = document.getElementById('myModal2');
let deleteCsrfToken;
let id;

Array.from(deleteBookBtns).forEach(btn => {
    btn.addEventListener('click', () => {
        id = btn.id;
        $.ajax({
            type: 'GET',
            url: `/deletebook/${id}`,
            success: (res) => {
                deleteCsrfToken = res.csrf_token;
            }
        });
    });
});

const delBtn = document.getElementsByClassName('delBtn')[0];
delBtn.addEventListener('click', () => {
    $.ajax({
        type: 'POST',
        data: { 'csrfmiddlewaretoken': deleteCsrfToken },
        url: `/deletebook/${id}`,
        success: (res) => {
            deleteBookModal.classList.remove('show');
            deleteBookModal.style.display = 'none';
            successAlert();
        }
    });
});
