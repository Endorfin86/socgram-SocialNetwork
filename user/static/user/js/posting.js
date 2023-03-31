    // Замена пользователя на request.user при добавлении поста
    let select = document.getElementById("id_athor")
    let iduser = document.getElementById("iduser")
    content = iduser.innerHTML
    for(let i = 0; i < select.length; i++) {
        if(select[i].value == content)
            select[i].setAttribute('selected', 'selected');
    }
    select.style.position = 'absolute'
    select.style.left = '-9999px'

    // Удаление поста
    // В ссылке или кнопке которая удаляет нужно прописать вызов функции delpost и указать id - onClick="delpost(this.id)
    function delpost(click){
        $.ajax ({
            type: "GET",
            url: 'del_post/',
            data: {
                "post_id": click,
            },
            dataType: 'text',
            cache: false,
            success: function(data) {
                if (data == 'no') {
                    console.log('Ошибка удаления');
                    }
                else {
                    idbtn = '#' + click
                    var idpost = $(idbtn).parent().parent().parent().attr("id")
                    var idp = '#' + idpost 
                    $(idp).slideUp()
                    }
                }
            });
    };

    // Лайки
    function like(click){
        let count = 'l' + click
        let likecount = document.getElementById(count).innerHTML
        $.ajax ({
            type: "GET",
            url: 'like/',
            data: {
                "post_id": click,
            },
            dataType: 'text',
            cache: false,
            success: function(data) {
                if (data == 'minus') {
                    console.log('Лайк снят');
                    likeint = parseInt(likecount) - 1
                    document.getElementById(count).innerHTML = likeint
                    }
                else {
                    console.log('Лайк добавлен');
                    likeint = parseInt(likecount) + 1
                    document.getElementById(count).innerHTML = likeint
                    }
                }
            });
    }