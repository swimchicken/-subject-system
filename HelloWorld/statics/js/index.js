
/*深色模式function(),上次沒做到的這次做到了!!*/
let darkmode = document.querySelector('#darkmode-icon');

darkmode.onclick = () => {
    /*這裡有bug尚未找到,不清楚如何替換icon,但由於錯誤的話整個js都無法啟動,所以
    先保留下次修理 */
    darkmode.classList.toggle('fa-sun-bright');
    document.body.classList.toggle('dark-mode');
}



const wrapper = document.querySelector(".wrapper");
const btnPopup = document.querySelector(".btnLogin-popup");


btnPopup.onclick = () => {
    wrapper.classList.add("active-popup");
}

const iconclose = document.querySelector(".icon-close");

iconclose.onclick = () => {
    wrapper.classList.remove("active-popup");
}
function selectTitle(titleNum){
    var titles = document.getElementsByTagName("h3");
    var chats = document.getElementsByTagName("h4");
        for (var i = 0; i < titles.length; i++) {
            titles[i].classList.remove("selected");
            titles[i].classList.add("unselected");
            chats[i].classList.remove("choose_label");
            chats[i].classList.add("unchoose_label");
        }
        // 再將被點擊的標題設定為選中狀態
        var selectedTitle = document.getElementById("title" + titleNum);
        var chat2 = document.getElementById("chat" + titleNum);
        selectedTitle.classList.add("selected");
        selectedTitle.classList.remove("unselected");
        chat2.classList.add("choose_label");
        chat2.classList.remove("unchoose_label");
}







var displayArea = document.getElementById('displayArea');

function hideDisplayArea(event) {
    if (!displayArea.contains(event.target)) {
        displayArea.style.display = 'none';
    }
}

document.addEventListener('click', hideDisplayArea);



function showDisplayArea() {
    if (displayArea.style.display === 'none') {
      setTimeout(function() {
        displayArea.style.display = 'block';
      }, 100);
    }
}


const form1 = document.getElementById("chat1");

form1.addEventListener("submit",(event) => {
    event.preventDefault();
    const selectValue1 = document.getElementById('uni').value;
    const selectValue2 = document.getElementById('bui').value;
    const selectValue3 = document.getElementById('dep').value;
    const selectValue4 = document.getElementById('cla').value;
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ selectValue ,selectValue2 ,selectValue3 ,selectValue4})
    })
    .then(response => response.json())
    .then(data => {
      // 在HTML中顯示搜尋結果
        const resultElement = document.getElementById('searchResult');
        resultElement.textContent = data.result;
    })
    .catch(error => {
        console.error('搜尋失敗', error);
    });
});
