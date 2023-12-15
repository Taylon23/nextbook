$(document).ready(function () {
    $('#favoritar-btn').click(function () {
        const livroId = $('#favoritar-form').data('livro-id');
        const isFavoritado = $('#favoritar-btn i').hasClass('fas'); // Verifica se está favoritado

        $.ajax({
            url: `/favoritar-livro/${livroId}/`,
            type: 'GET',
            success: function (response) {
                if (response.status === 'ok') {
                    if (isFavoritado) {
                        $('#favoritar-btn i').removeClass('fas').addClass('far');
                        $('#favoritar-btn').html('<i class="far fa-star"></i> Favoritar');
                    } else {
                        $('#favoritar-btn i').removeClass('far').addClass('fas');
                        $('#favoritar-btn').html('<i class="fas fa-star"></i> Desfavoritar');
                    }
                } else {
                    if (confirm('Você deve estar logado para favoritar. Clique OK para ir à página de login.')) {
                        const returnUrl = window.location.href; // Obtém a URL atual
                        window.location.href = `/login?next=${encodeURIComponent(returnUrl)}`; // Redireciona para a página de login com 'next' como a URL atual
                    }
                }
            },
            error: function () {
                alert('Erro ao processar a requisição.');
            }
        });
    });
});
