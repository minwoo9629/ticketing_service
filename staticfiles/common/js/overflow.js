const html = document.querySelector('html');
const body = document.querySelector('body');
let path = location.pathname;
if (path === "/") {
    html.classList.add('overflow');
    body.classList.add('overflow');
} else {
    html.classList.remove('overflow');
    body.classList.remove('overflow');
    html.style.overflowX = 'hidden';
}
