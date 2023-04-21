

const wrapper = document.querySelector(".wrapper");
const btnPopup = document.querySelector(".btnLogin-popup");


btnPopup.onclick = () => {
    wrapper.classList.add("active-popup");
}

const iconclose = document.querySelector(".icon-close");

iconclose.onclick = () => {
    wrapper.classList.remove("active-popup");
}
