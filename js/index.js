

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
        for (var i = 0; i < titles.length; i++) {
          titles[i].classList.remove("selected");
        }
        // 再將被點擊的標題設定為選中狀態
        var selectedTitle = document.getElementById("title" + titleNum);
        selectedTitle.classList.add("selected");
}