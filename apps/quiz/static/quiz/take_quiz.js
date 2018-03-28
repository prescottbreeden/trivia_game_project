console.log('Power Overwhelming...')

$(document).ready(function(){

$('button').on('click', function(){
    if ($(this).val() == '1'){
        $('.answer').html(
            '<h1 class="correct">CORRECT!!</h1>'
            )
    }
    else {
        $('.answer').html(
            '<h1 class="incorrect">Incorrect...</h1>'
            )
    }
})
})