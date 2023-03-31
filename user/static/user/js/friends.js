// Добавить в друзья
function addfriend(user){
    $.ajax ({
        type: "GET",
        url: '/friends/add',
        data: {
            "user_id": user,
        },
        dataType: 'text',
        cache: false,
        success: function(data) {
            if (data == 'yesplus') {
                console.log('Вы подписались');
                document.getElementById("friend").innerHTML = '<button id={{ profile.user.pk }} type="button" onClick="delfriend(this.id)"><i class="fa-solid fa-user-minus white-text"></i>&nbsp; Удалить из друзей</button>'
                }
            else {
                console.log('Ошибка добавление');
                }
            }
        });
}

// Удалить из друзей
function delfriend(user){
    $.ajax ({
        type: "GET",
        url: '/friends/del',
        data: {
            "user_id": user,
        },
        dataType: 'text',
        cache: false,
        success: function(data) {
            if (data == 'yesminus') {
                console.log('Вы отписались');
                document.getElementById("friend").innerHTML = '<button id={{ profile.user.pk }} type="button" onClick="addfriend(this.id)"><i class="fa-solid fa-user-plus white-text"></i>&nbsp; Добавить в друзья</button>'
            }
            else {
                console.log('Ошибка удаление');
                }
            }
        });
}

// Удалить из друзей в профиле в боковой панели
function delfriendprofile(user){
    $.ajax ({
        type: "GET",
        url: '/friends/del',
        data: {
            "user_id": user,
        },
        dataType: 'text',
        cache: false,
        success: function(data) {
            if (data == 'yesminus') {
                console.log('Вы отписались');
                let idlink = '#link' + user 
                $(idlink).slideUp()
            }
            else {
                console.log('Ошибка удаление');
                }
            }
        });
}