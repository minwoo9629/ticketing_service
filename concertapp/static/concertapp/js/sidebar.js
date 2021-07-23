// let contentNum = 0;
// let totalNum = 0;
// let sideContent, pointBtnAll, pointInnerAll;
// let pauseBtn, icon;
// let timerId;
// let flag = true;
let contentNum = 0;
let timerId;
let flag = true;
const sideContent = document.querySelectorAll('.sideContent');
const pointBtnAll = document.querySelectorAll('.pointWrap li');
const pointInnerAll = document.querySelectorAll('.pointWrap li .inner');
const descriptionAll = document.querySelectorAll('.sideDesc');
const pauseBtn = document.querySelector('.pauseBtn');
const icon = document.querySelector('.pauseBtn i')
const totalNum = sideContent.length;
        
for (let i = 0; i < pointBtnAll.length; i++) {
    (function (idx) {
        pointBtnAll[idx].onclick = () => {
            contentNum = idx;
            contentChangeFunc();
        }
    })(i);
}
contentChangeFunc();
if (pauseBtn){
    pauseBtn.addEventListener('click', () => {
        contentPauseFunc()
    })
}
function nextContent() {
    if (contentNum < totalNum - 1) {
        contentNum++;
    } else {
        contentNum = 0;
    }
    contentChangeFunc();
}

function contentChangeFunc() {
    for (var i = 0; i < totalNum; i++) {
        if (contentNum == i) {
            sideContent[i].classList.add("active");
            pointBtnAll[i].classList.add("active");
            pointInnerAll[i].classList.add("active");
            descriptionAll[i].classList.add("active");
        } else {
            sideContent[i].classList.remove("active");
            pointBtnAll[i].classList.remove("active");
            pointInnerAll[i].classList.remove("active");
        }
    }
}

function contentPauseFunc() {
    if (flag === true) {
        clearInterval(timerId)
        icon.classList.add("fa-play")
        icon.classList.remove("fa-pause")
        flag = false
    } else {
        icon.classList.add("fa-pause")
        icon.classList.remove("fa-play")
        flag = true
        timerId = setInterval(nextContent, 4000)
    }

}
timerId = setInterval(nextContent, 4000)