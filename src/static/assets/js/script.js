function open_close_GM_costum_modal(trigger) {
    var modal = document.getElementById(trigger.dataset.modalTargget);
    var holder = modal.parentElement;
    if (holder.classList.contains("active")) {
        holder.classList.remove("active");
        modal.classList.remove("active");
    } else {
        holder.classList.add("active");
        modal.classList.add("active");
    }
}

function close_GM_modal_btns(btn) {
    var modal = btn.parentElement.parentElement;
    var holder = modal.parentElement;
    holder.classList.remove("active");
    modal.classList.remove("active");
}


