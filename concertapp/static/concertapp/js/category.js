const moreWrap = document.querySelector('.moreWrap')
const moreBtn = document.querySelector('.moreBtn');
const locationCategory = document.location.pathname.split('/')[2];
const categoryList = document.querySelector('.categoryList');
const categoryCard = document.querySelectorAll('.categoryCard');
let start_idx, end_idx;
start_idx = 12
end_idx = 18

if (moreWrap && categoryCard.length !== 12) {
    moreWrap.style.display = 'none';
}
if (moreBtn) {
    moreBtn.addEventListener('click', () => {
        $.ajax({
            url: `/api/${locationCategory}/`,
            method: "GET",
            data: { start_idx: start_idx, end_idx: end_idx },
            dataType: "json",
        }).done(response => {
            if (response.length !== 6) {
                moreWrap.style.display = 'none';
            }
            for (let i = 0; i < response.length; i++) {
                let newCardDiv = document.createElement('div');
                newCardDiv.setAttribute('class', 'categoryCard');
                let newAnchor = document.createElement('a');
                newAnchor.setAttribute('href', `/performance/detail/${response[i].id}`)
                let newImg = document.createElement('img');
                newImg.setAttribute('src', `${response[i].poster}`)
                let newTitle = document.createElement('p');
                newTitle.innerText = response[i].title
                newCardDiv.appendChild(newAnchor)
                newAnchor.appendChild(newImg)
                newAnchor.appendChild(newTitle)
                categoryList.appendChild(newCardDiv);
            }
        }).fail(error => {
            console.log(error)
        })
        start_idx += 6
        end_idx += 6
    })
}