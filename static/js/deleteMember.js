const deleteMemberBtns = document.getElementsByClassName('deleteMemberBtn');
const deleteMemberModal = document.getElementById('myModal2');
let deleteMemberCsrfToken;
let memberId1;

Array.from(deleteMemberBtns).forEach(btn => {
    btn.addEventListener('click', (e) => {
        memberId1 = btn.id;
        deleteMemberModal
        $.ajax({
            type: 'GET',
            url: `/deletemember/${memberId1}`,
            success: (res) => {
                console.log(res);
                deleteMemberCsrfToken = res.csrf_token;
            }
        });
    });
});

const delBtn1 = document.getElementsByClassName('delBtn')[0];
delBtn1.addEventListener('click', (e) => {
    $.ajax({
        type: 'POST',
        data: { 'csrfmiddlewaretoken': deleteMemberCsrfToken },
        url: `/deletemember/${memberId1}`,
        success: (res) => {
            console.log(res);
            deleteMemberModal.classList.remove('show');
            deleteMemberModal.style.display = 'none';
            successAlert(res.success);
        }
    });
});
