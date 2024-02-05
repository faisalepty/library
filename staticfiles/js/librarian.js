const updateLibrarian = document.querySelectorAll('.updatelibrarian');
const deleteLibrarianModal = document.getElementById('myModal2');
const ldeleteBtn = document.querySelectorAll('.deleteLibrarianBtn')
const ldelete = document.querySelector('.delBtn');
const librarianModal = document.getElementById('myModal6');
const ldata = document.getElementById('ldata');
const lfirstName = librarianModal.querySelector('[name="first_name"]');
const llastName = librarianModal.querySelector('[name="last_name"]');
const lemail = librarianModal.querySelector('[name="email"]');
const lpassword1 = librarianModal.querySelector('[name="password1"]');
const lpassword2 = librarianModal.querySelector('[name="password2"]');
const lcsrfMIddlewareToken = document.getElementById('modal6csrf_token').firstChild;
const laddBtn = document.getElementById('addLibrarian');
const lupdateBtn = document.getElementById('updateLibrarian');
let pk
updateLibrarian.forEach(btn => {
  btn.addEventListener('click', (e) => {
    pk = e.target.id
    $.ajax({
      type: 'GET',
      url: `/editlibrarianinfo/${pk}`,
      success: (res) => {
     
        lfirstName.value = res.librarian.first_name
        llastName.value = res.librarian.last_name
        lemail.value = res.librarian.email
        lpassword2.style.display = 'none'
        laddBtn.classList.add('d-none')
        lupdateBtn.classList.remove('d-none')
      }
    })
  })
})


lupdateBtn.addEventListener('click', (e) => {
  const datar = {
    'csrfmiddlewaretoken': lcsrfMIddlewareToken.value,
    'first_name': lfirstName.value,
    'last_name': llastName.value,
    'email': lemail.value,
    'password1': lpassword1.value,
  }
    $.ajax({
      type: 'POST',
      url: `/editlibrarianinfo/${pk}`,
      data: datar,
      success: (res) =>{
    
        if (res.success){
          librarianModal.classList.remove('show')
      librarianModal.style.display = 'none'
          successAlert(res.success)
        }else if(res.error){
         
          librarianModal.classList.remove('show')
      librarianModal.style.display = 'none'
          errorAlert(res.error)
        }
      },
      error: (res) => {
        librarianModal.classList.remove('show')
      librarianModal.style.display = 'none'
        errorAlert(res.error)
      }
    })
})


ldeleteBtn.forEach(btn => {
  btn.addEventListener('click', (e) => {
  pk = e.target.id
})})

ldelete.addEventListener('click', (e) => {
    $.ajax({
      type: 'POST',
      url: `/deletelibrarian/${pk}`,
      data: {'csrfmiddlewaretoken': lcsrfMIddlewareToken.value},
      success: (res) => {
        deleteLIbrarianModal.classList.remove('show');
            deleteLIbrarianModal.style.display = 'none';
            successAlert(res.success);
      }
    })
})

laddBtn.addEventListener('click', (e) => {
  const datar = {
    'csrfmiddlewaretoken': lcsrfMIddlewareToken.value,
    'first_name': lfirstName.value,
    'last_name': llastName.value,
    'username': lfirstName.value,
    'email': lemail.value,
    'password1': lpassword1.value,
    'password2': lpassword2.value
  }
  $.ajax({
    type: 'POST',
    url: '/librarians/',
    data: datar,
    success: (res) => {
     
      if(res.Success){
    
        successAlert(res.Success)
       librarianModal.classList.remove('show')
     librarianModal.style.display = 'none'
        dataInnerHtml = ` <li class="d-flex">
            <p style="width: 20%;" class="text-start">${ res.id }</p>
            <p style="width: 20%;" class="text-start ps-5">${ datar.username } ${ datar.last_name }</p>
            <p style="width: 20%;" class="text-start">${ datar.email }</p>
            <p></p>
                <div class="dropdown" style="left: 17%;">
                <a href="#" role="button" data-bs-toggle="dropdown" class="action" data-bs-target="#c" >
                ...
               </a>
               <ul  id="c" class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                <li type="button" data-bs-toggle="modal" data-bs-target="#myModal5">
                  <a class="dropdown-item" href="#">
                  <p class="updateBookStatus" style="font-size:0.8em;"  id="{{transaction.copyId}}" amount="{{ transaction.book.fee }}">Update</p>
                </a>
                </li>
                <li>
                    <a class="dropdown-item" href="">
                    <p class="updatememberBtn" style="font-size: 0.8em;" type="button" id="{{transaction.member.member_id }}">Member details</p>
                  </a>
                  </li>
                </ul>
                
              
            </div>
           
        </li>
        <hr>`
        ldata.innerHTML += dataInnerHtml
      }else if (res.error){
        librarianModal.classList.remove('show')
     librarianModal.style.display = 'none'
        errorAlert(res.error)
      }
      
    },
    error: (res) => {
      librarianModal.classList.remove('show')
     librarianModal.style.display = 'none'
      errorAlert(res.error)
    }
  })

})



