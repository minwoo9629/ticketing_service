const menuBtn = document.querySelector('.toggleBtn');
const menu = document.querySelector('.navbar_menu');
const userDropDownBtn = document.querySelector('.userDropDownBtn');
const userDropDownMenu = document.querySelector('.userDropDownMenu');
    
// toggle Event
menuBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
})
if(userDropDownBtn){
    userDropDownBtn.addEventListener('click', (event) => {
        event.stopPropagation();
        userDropDownMenu.classList.toggle('active');
    })
}

document.addEventListener('click', () => {
    userDropDownMenu.classList.remove('active');
})