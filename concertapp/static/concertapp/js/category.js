const moreWrap = document.querySelector('.moreWrap')
const moreBtn = document.querySelector('.moreBtn');
const locationCategory = document.location.pathname.split('/')[2];
const categorySection = document.querySelector('.categorySection');
let start_idx, end_idx;
start_idx = 10
end_idx = 15
moreBtn.addEventListener('click', () => {
    $.ajax({
        url: `/api/${locationCategory}/`,
        method: "GET",
        data: { start_idx: start_idx, end_idx: end_idx },
        dataType: "json",
    }).done(response => {
        let newDiv = document.createElement('div');
        newDiv.setAttribute('class', 'categoryList');
        if (response.length === 5) {
            newDiv.classList.add('active');
        } else {
            moreWrap.style.display = 'none';
        }
        for (let i = 0; i < response.length; i++) {
            let newInnerDiv = document.createElement('div');
            newInnerDiv.setAttribute('class', 'categoryCard');
            newDiv.appendChild(newInnerDiv)
            let newAnchor = document.createElement('a');
            console.log(response[i].id)
            newAnchor.setAttribute('href', `/performance/detail/${response[i].id}`)
            let newImg = document.createElement('img');
            newImg.setAttribute('src', `${response[i].poster}`)
            let newTitle = document.createElement('p');
            newTitle.innerText = response[i].title
            newInnerDiv.appendChild(newAnchor)
            newAnchor.appendChild(newImg)
            newAnchor.appendChild(newTitle)
            categorySection.insertBefore(newDiv, moreWrap)
     }
    }).fail(error => {
        console.log(error)
    })
    start_idx += 5
    end_idx += 5
})


const categoryList = document.querySelectorAll('.categoryList');
for (let i = 0; i < categoryList.length; i++) {
    if (categoryList[i].childElementCount === 5) {
        categoryList[i].classList.add('active')
    } else {
        moreWrap.style.display = 'none';
    }
}