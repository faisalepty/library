function successAlert(success){
    const successmodal = document.getElementById('myModal4');
    const backdrop = document.getElementsByClassName('modal-backdrop')
    [0];
    const type = document.querySelector('.type')
    const message = document.querySelector('.message')
    const body = document.getElementsByTagName('body')[0];
    
    successmodal.classList.add('show');
    successmodal.style.display = 'block'
    
    type.classList.add('bi', 'bi-check-circle')
    type.style.backgroundColor = 'rgb(135, 221, 154)'
    type.style.color = 'green'
    message.innerText = success
    setTimeout(function(){
      successmodal.classList.remove('show')
      body.classList.remove('modal-open')
      successmodal.style.display = 'none'
      body.style = ''
      backdrop.remove()
    }, 2000)
  }
  
  
  function errorAlert(error){
    const errormodal = document.getElementById('myModal4');
    const backdrop = document.getElementsByClassName('modal-backdrop')
    [0];
    const type = document.querySelector('.type')
    const message = document.querySelector('.message')
    const body = document.getElementsByTagName('body')[0];
  
    type.classList.add('bi', 'bi-exclamation-triangle')
    type.style.backgroundColor = 'rgb(224, 165, 165)'
    type.style.color = 'red'
    message.innerText = error
    errormodal.classList.add('show');
    errormodal.style.display = 'block'
    setTimeout(function(){
      errormodal.classList.remove('show')
      body.classList.remove('modal-open')
      errormodal.style.display = 'none'
      body.style = ''
      backdrop.remove()
    }, 2000)
  }