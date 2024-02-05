const updateMemberModal = document.getElementById('myModal1');
const updateMemberBtns = document.getElementsByClassName('updateMemberBtn');
const updateMemberBtnArr = [...updateMemberBtns];
let memberId;

const formInputs1 = ['first_name', 'last_name', 'gender', 'age', 'address', 'mobile_no', 'email', 'national_id'];

const resetMemberInputs1 = () => {
    formInputs1.forEach(inputName => {
        const input = document.getElementsByName(inputName)[0];
        input.value = '';
    });
    imgField.querySelector('img').classList.add('d-none');
    imgField.querySelector('label').classList.remove('d-none');
    imgField.querySelector('input').classList.remove('d-none');
};

updateMemberBtnArr.forEach(btn => {
    btn.addEventListener('click', (e) => {
        memberId = e.target.id;

        $.ajax({
            type: 'GET',
            url: `/editmemberinfo/${memberId}`,
            success: (res) => {

                const first_nameInput = document.getElementsByName('first_name')[0];
                const last_nameInput = document.getElementsByName('last_name')[0];
                const genderInput = document.getElementsByName('gender')[0];
                const ageInput = document.getElementsByName('age')[0];
                const addressInput = document.getElementsByName('address')[0];
                const mobile_noInput = document.getElementsByName('mobile_no')[0];
                const emailInput = document.getElementsByName('email')[0];
                const national_idInput = document.getElementsByName('national_id')[0];
                // const photoInput = document.getElementById('imageFile');
                const imgField = document.getElementById('imgField');
                const csrfTokenInput = document.getElementById('modal1csrf_token').firstChild;

                first_nameInput.value = `${res.data.first_name}`;
                last_nameInput.value = `${res.data.last_name}`;
                genderInput.value = `${res.data.gender}`;
                ageInput.value = `${res.data.age}`;
                addressInput.value = `${res.data.address}`;
                mobile_noInput.value = `${res.data.mobile_no}`;
                emailInput.value = `${res.data.email}`;
                national_idInput.value = `${res.data.national_id}`;

                const updatememberbtn = document.getElementById('updateMember');
                const addmemberbtn = document.getElementById('addmember');
                updatememberbtn.classList.remove('d-none');
                addmemberbtn.classList.add('d-none');
                updateMemberModal.getElementsByClassName('modal-title')[0].firstChild.innerText = 'UPDATE MEMBER'

            },
            error: (res) => {
            }
        });
    });
});

const updateMemberBtn = document.getElementById('updateMember');
updateMemberBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('csrfmiddlewaretoken', csrfTokenInput.value);
    formInputs1.forEach(inputName => {
        const input = document.getElementsByName(inputName)[0];
        formData.append(inputName, input.value);
    });
    formData.append('debt', 0);
    formData.append('profile_img', photoInput.files[0]);

    $.ajax({
        type: 'POST',
        url: `/editmemberinfo/${memberId}`,
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        data: formData,
        success: (res) => {
            if(res.success){
            resetMemberInputs1();
            updateMemberModal.classList.remove('show');
            updateMemberModal.style.display = 'none';
            successAlert();
        }else if(res.error){
            errorAlert(res.error)
        }
    },
        error: (res) => {
        }
    });
});
