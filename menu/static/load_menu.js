$('li').click(function() {
            $('#dishes').empty();
            $.ajax({
                url: 'http://127.0.0.1:8000/menus/' + this.id + '/',
                contentType: 'application/json; charset=UTF-8',
                success: function(data){
                    $('#menuName').text(data.name);
                    $('#menuDescription').text(data.description);
                    $('#menuPrepared').text(data.prepared);
                    $('#menuPrice').text(data.price);
                    var dishes = data.dishes;
                    content = ''
                    for (var i in dishes) { content += '<li>' + dishes[i].name + '</li>'; }
                    $('#dishes').html(content);
                        }
                });
        });