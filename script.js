$(function() {
    $('#calculate').click(function(){
        $("#result").html("yolo");
        $.ajax({
            url: '/addnumber',
            data:{
                a: $('#a').val(),
                b: $('#b').val()
            },
            dataType: 'JSON',
            type: 'GET',
            success: function(data){
                $("#result").html(data.result);
            }
        }).fail(function() {
            $("#result").html("yo");
        });
    });
});
