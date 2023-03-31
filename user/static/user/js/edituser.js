// Форма редактирования пользователя
let btn = document.getElementById("btn-edit")
let closeedit = document.getElementById("btn-close")
let formedit = document.getElementById("form-edit")
let bgformedit = document.getElementById("bg-form-edit")
btn.addEventListener('click', edit);
closeedit.addEventListener('click', close);
bgformedit.addEventListener('click', close);
function edit(){
    formedit.style.display = 'block'
    bgformedit.style.display = 'block'
}
function close(){
    formedit.style.display = 'none'
    bgformedit.style.display = 'none'
}

// Логин=Идентификатор
let username = document.getElementById("id_username")
let slug = document.getElementById("id_slug")
username.addEventListener('input', inputslug);
function inputslug(){slug.value = username.value}