const searchform = document.getElementById('searchform');
const icon = document.getElementById('qtoggleicon');
const closeicon = document.getElementById('closeicon');
const filterDropdown = document.getElementById('filterDropdown');
const searchBtn1 = document.getElementById('searchBtn');
const activeLink = document.querySelector('#activeLink').firstElementChild.nextElementSibling;
const addMemberBtn1 = document.getElementsByClassName('addMemberBtn')[0];
const addBookBtn1 = document.getElementsByClassName('addBookBtn')[0];
const logoutbtn = document.getElementsByClassName('logout')[0];


icon.addEventListener('click', (e) => {
  searchform.style.display = 'block'
  searchBtn1.style.display = 'block'
  closeicon.style.display = 'block'
  filterDropdown.style.display = 'block'
  addMemberBtn1.style.display = 'none'
  addBookBtn1.style.display = 'none'
  icon.style.display = 'none'
  logoutbtn.style.display = 'none'
  // activeLink.style.display = 'none'
})

closeicon.addEventListener('click', (e) =>{
  searchform.style.display = ''
  searchBtn1.style.display = ''
  filterDropdown.style.display = ''
  closeicon.style.display = ''
  addMemberBtn1.style.display = ''
  addBookBtn1.style.display = ''
  icon.style.display = ''
  logoutbtn.style.display = ''
  // activeLink.style.display = ''
})






const DSearchForm = document.getElementById('searchform');
const btnSearch = document.getElementsByClassName('bi-search')[0];
const searchfilterBtn = document.getElementById('searchFilter');
const searchFilterDrpDown = document.getElementById('searchFilterDrpDown');
const searchChildNodesArr = Array.from(searchFilterDrpDown.childNodes);
const searchType = document.getElementsByName('searchType')[0];

searchChildNodesArr.forEach(child => {
  child.addEventListener('click', (e) => {
    searchfilterBtn.innerText = e.target.innerText
    searchType.value = e.target.id
  })
})



const sideNav = document.getElementById('nav');
sideNav.addEventListener('mouseover', (e) => {
  Array.from(sideNav.children).forEach(element => {
    if (element.classList.contains('navborder')){
    element.style.paddingRight = '35px'
  }else{
    element.style.paddingRight = '30px'
  }
      element.firstElementChild.style.display = 'block';
      sideNav.style.width = '100px'
  });
});
sideNav.addEventListener('mouseout', (e) => {
  Array.from(sideNav.children).forEach(element => {
    if (element.classList.contains('navborder')){
    element.style.paddingRight = '17px'
  }
  element.style.paddingRight = '20px'
      element.firstElementChild.style.display = 'none'; 
      sideNav.style.width = '55px'  
  });
});  

const searchPlaceHolder = document.getElementById('searchform');
const searchType1 = document.getElementById('searchFilterDrpDown');
const inputs = document.getElementsByTagName('input');

Array.from(inputs).forEach(input => {
    input.setAttribute('autocomplete', 'off')
})

Array.from(searchType1.childNodes).forEach(type => {
  type.addEventListener('click', (e) => {
    searchPlaceHolder.placeholder = `Search by ${e.target.innerText}`
    if (e.target.innerText == 'All'){
      searchPlaceHolder.placeholder = 'Search by Title, Author'
    }else if(e.target.innerText == 'Member'){
      searchPlaceHolder.placeholder = 'Search by Name'
    }
    
  })
})




