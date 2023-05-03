

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
    var titles = document.getElementsByTagName("h2");
    var chats = document.getElementsByTagName("h3");
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


