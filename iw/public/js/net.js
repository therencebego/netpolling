$(window).load((function()
                {
                   $("a.menu").on("click", function()
                                           {
                                               $.ajax({
                                                   type: 'post',
                                                   data:
                                                    {
                                                       id:this.id
                                                    },
                                                   url: 'control.php',
                                                   timeout: 3000,
                                                   success:function(data)
                                                   {
                                                       $("#main").html(data)
                                                   },
                                                   error: function()
                                                   {
                                                       alert('La requête n\'a pas abouti');
                                                   }
                                               })
                                           });
                })());

