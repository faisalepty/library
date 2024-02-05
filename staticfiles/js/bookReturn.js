const updateStatus = document.querySelectorAll('.updateBookStatus');
const updateStatusModal = document.getElementById('myModal5');
const updateStatusBtn = document.getElementById('updateStatusBtn');
const updateStatusCsrfToken = document.getElementById
('updateStatusCsrfToken');
const Status = document.getElementsByClassName('status')[0];
const copyQuantity = document.getElementsByClassName('copyQuantity')[0];
const Debt = document.getElementsByClassName('debt')[0];
const amountPaid = document.getElementById('amntPaid');
const amount = document.getElementById('amount');
let copyId
let paid
let currentStatus
updateStatus.forEach(btn => {
  btn.addEventListener('click', (e) => {
    currentStatus = e.target.parentElement.parentElement.parentElement.parentElement.parentElement.getElementsByClassName('status')[0];
    copyId = e.target.id
    paid = e.target.getAttribute('amount')
    amount.innerText = `ksh ${e.target.getAttribute('amount')}`
    amountPaid.setAttribute('max', e.target.getAttribute('amount'))
  })
})
updateStatusBtn.addEventListener('click', (e) => {
  
  $.ajax({
    type: 'POST',
    data: {'csrfmiddlewaretoken': updateStatusCsrfToken.firstElementChild.value, 'amountPaid': amountPaid.value},
    url: `/updatebookreturn/${copyId}`,
    success: (res) => {
      updateStatusModal.classList.remove('show')
      updateStatusModal.style.display = 'none'
      
      if(copyQuantity){
        (copyQuantity.innerText, parseInt(copyQuantity.innerText))
      copyQuantity.innerText = parseInt(copyQuantity.innerText) + 1
     
      }
      if(currentStatus){
        currentStatus.innerText = 'returned'
      }
      if(Debt){
       Debt.innerText = parseInt(Debt.innerText) - paid
      }
      
      successAlert(res.success)
    }
  })
})
