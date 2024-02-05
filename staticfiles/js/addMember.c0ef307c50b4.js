const addMemberFormBtn = document.getElementById('addmember');
const photoInput = document.getElementById('imageFile');
const imgField = document.getElementById('imgField');
const csrfTokenInput = document.getElementById('modal1csrf_token').firstChild;
const memberModal = document.getElementById('myModal1');

const formData = new FormData();
const formInputs = ['first_name', 'last_name', 'gender', 'age', 'address', 'mobile_no', 'email', 'national_id'];

const resetMemberInputs = () => {
    formInputs.forEach(inputName => {
        const input = document.getElementsByName(inputName)[0];
        input.value = '';
    });
    imgField.querySelector('img').classList.add('d-none');
    imgField.querySelector('label').classList.remove('d-none');
    imgField.querySelector('input').classList.remove('d-none');
};

const updatememberbtn = document.getElementById('updateMember');
const addmemberbtn = document.getElementById('addmember');
updatememberbtn.classList.add('d-none');
addmemberbtn.classList.remove('d-none');
memberModal.getElementsByClassName('modal-title')[0].firstChild.innerText = 'ADD MEMBER'

formInputs.forEach(inputName => {
    const inputs = document.getElementsByName(inputName);
    inputs.forEach(input => {
        input.addEventListener('change', (e) => {
            formData.append(inputName, input.value);
        });
    });
});

formData.append('debt', 0);
formData.append('csrfmiddlewaretoken', csrfTokenInput.value);

photoInput.addEventListener('change', () => {
    formData.append("profile_img", photoInput.files[0]);
    if (photoInput.files.length > 0) {
        imgField.childNodes.forEach(node => {
            if (node.nodeType === 1) { 
                node.classList.add('d-none');
            }
        });
        const lastChild = imgField.lastChild;
        if (lastChild.previousSibling) {
            lastChild.previousSibling.classList.remove('d-none');
        } 
    }
});

addMemberFormBtn.addEventListener('click', (e) => {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/newmember/',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        },
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        data: formData,
        success: (res) => {
            if (res.success){
            resetMemberInputs();
            memberModal.classList.remove('show');
            memberModal.style.display = 'none';
            successAlert(res.success);
        }else if (res.error){
            memberModal.classList.remove('show');
            memberModal.style.display = 'none';
            errorAlert(res.error)
        }
    },
        error: (res) => {
            memberModal.classList.remove('show');
            memberModal.style.display = 'none';
            errorAlert(res.error)
        }
    });
});
