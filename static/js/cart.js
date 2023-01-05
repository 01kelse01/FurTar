$(document).ready(() => {
    console.log('cart.js -> start');

    $('#products').on('click', '.add-to-cart-btn', (event) => {
       console.log('add to cart -> click');
       //
        const userId = $('#user_id').val();
        console.log('userId -> ' + userId);
        //
        if (userId == 'None') {
            alert('Для використання кошика Ви маєте авторизуватись!');
            // window.location = '/accounts/sign_in';
        } else {
            let productId = $(event.target).prev().val();

            console.log('productId -> ' + productId);

            // AJAX - запит на збереження товару в БД
            $.ajax({
                url: '/cart/ajax_cart',
                data: `userId=${userId}&productId=${productId}`,
                success: (response) => {
                    console.log(response.message);
                    $('#cart_count').text(response.count);
                    $('.cart-summary').find('h4').text('Товарів обрано: ' + response.count);
                    $('.cart-summary').find('h5').text('Загальна вартість: ' + response.amount + ' грн');
                }
            });
        }
    });
});