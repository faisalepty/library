
const issueBookModal = document.getElementById('myModal3')
const issueBookBtn = document.getElementsByClassName('issueBookBtn');
const bookInput = document.getElementById('bookInput');
const dateInput = document.getElementById('dateInput');
const postIssueBookBtn = document.getElementById('postIssueBookBtn');
const modal3csrf_token = document.getElementById('modal3csrf_token');
const memberInput = document.getElementById('memberInput');
const bookDropDown = document.getElementById('bookDropDown');
const memberDropDown = document.getElementById('memberDropDown');
const issueBookBtnArr = [...issueBookBtn]
const BooksPTags =bookDropDown.getElementsByTagName('p');
const bookPtArr = [...BooksPTags]


postIssueBookBtn.addEventListener('click', (e) => {
  const data = {'book_title': bookInput.value,
                'first_name': memberInput.value.split(' ')[0],
                'last_name': memberInput.value.split(' ')[1],
                'return_date': dateInput.value,
                'csrfmiddlewaretoken': modal3csrf_token.innerText
                }

  $.ajax({
    type: 'POST',
    data: data,
    url:'/issuebook/',
    success: (res) => {
    
      issueBookModal.classList.remove('show')
      issueBookModal.style.display = 'none'
      if (res.success){
        successAlert(res.success)
        const copyCount = document.getElementById(`${data.book_title}`);
        copyCount.innerText = parseInt(copyCount.innerText) - 1
      }else if(res.error){ 
       errorAlert(res.error)
      }
     
    },
    error: (res) => {
      issueBookModal.classList.remove('show')
      issueBookModal.style.display = 'none'
      console.log(res)
      errorAlert(res.statusText)
    } 

  })
})



const setDropdownValues = (dropdown, input, queryKey) => {
  dropdown.addEventListener('click', (e) => {
    if (e.target.tagName === 'P') {
      input.value = e.target.innerText;
      e.target.style.display = 'none';
    }
  });

  document.addEventListener('click', (e) => {
    if (!dropdown.contains(e.target) && e.target !== input) {
      dropdown.style.display = 'none';
    }
  });

  input.addEventListener('input', (e) => {
    const query = e.target.value;
    dropdown.style.display = query ? 'block' : 'none';

    $.ajax({
      type: 'GET',
      url: '/issuebook/',
      data: { [queryKey]: query },
      success: (res) => {
        if (input.value !== '') {
        
        if(res.members){
            const dropdownHtml = res['members'].reduce((acc, item) => {
                return acc + `<p class='mb-0 ps-2' style="font-size: 0.5em; height: 14px; overflow: hidden;">${item}</p>`;
              }, '');
    
              dropdown.innerHTML = dropdownHtml;
        }else{
            const dropdownHtml = res['books'].reduce((acc, item) => {
                return acc + `<p class='mb-0 ps-2' style="font-size: 0.5em; height: 14px; overflow: hidden;">${item}</p>`;
              }, '');
    
              dropdown.innerHTML = dropdownHtml;
        }
         
        } else {
          dropdown.style.display = 'none';
        }
      },
    });
  });
};

setDropdownValues(memberDropDown, memberInput, 'r');
setDropdownValues(bookDropDown, bookInput, 'q');

issueBookBtnArr.forEach((btn) => {
  btn.addEventListener('click', (e) => {
    if (e.target.classList.contains('m')){
      bookInput.value = ''
      memberInput.value = e.target.id;
    }else{
       bookInput.value = e.target.id;
    memberInput.value = '';
    }
   
  });
});




