var cart = {};
var item = {};
item={'id_product': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'id_category': [1, 1, 1, 1, 1, 1, 1, 1, 1], 'name_of_product': ['Горшок из бетона', 'Горшок из бетона', 'Горшок из бетона', 'Горшок из бетона', 'Горшок из бетона', 'Свеча из бетона', 'Свеча из бетона', 'Свеча из бетона', 'Свеча из бетона'], 'product_description': ['Горшок для цветов', 'Горшок для кухни', 'Горшок для цветов', 'Горшок для цветов', 'Горшок для цветов', 'Свечи с ароматизатором', 'Свечи с ароматизатором', 'Свечи с ароматизатором', 'Свечи с ароматизатором'], 'image': ['горшок.jpg', 'горшок2.jpg', 'горшок3.jpg', 'горшок4.jpg', 'горшок5.jpg', 'Свечи ИЗ БЕТОНА .jpg', 'Свечи  ИЗ БЕТОНА2 .jpg', 'Свечи ИЗ БЕТОНА3 .jpg', 'Свечи ИЗ БЕТОНА4 .jpg'], 'price': [150, 120, 1500, 2000, 1200, 500, 700, 600, 550]}
function loadCart() {
    //проверяю есть ли в localStorage запись cart
    if (sessionStorage.getItem('cart')) {
        console.log("TEXt");
        cart = JSON.parse(sessionStorage.getItem('cart'));
            showCart();
        }
    else {
        $('.main-cart').html('Корзина пуста!');
    }
}

function showCart() {
    //вывод корзины
     if (!isEmpty(cart)) {
        $('.main-cart').html('Корзина пуста!');
    }
     else {
           var out = '';
           for (var id in cart) {
               console.log(id)
               out += '<div class="col-12 cart-item">';
               out += `<button data-id="${id}" class="del-goods">x</button>`;
               out += `<img class="cart-icon" src="../static/image_product/${item["image"][id]}">`;
               out += ` <p class="cart-name">${item["name_of_product"][id]}</p>`;
               /*out +=`<p class="name">${item["id_product"][id]}</p>`;*/
               out += '<div class="cart-count_wrapper">';
               out += `  <button data-id="${id}" class="minus-goods">-</button>  `;
               out += ` <p class="cart-count"> ${cart[id]} </p>`;
               out += `  <button data-id="${id}" class="plus-goods">+</button>  `;
               out += '</div>';
               out += `<p class="cart-price"> ${cart[id]*item["price"][id]}</p>`;
               out += '</div>';

           }
            $('.main-cart').html(out);
            $('.del-goods').on('click', delGoods);
            $('.plus-goods').on('click', plusGoods);
            $('.minus-goods').on('click', minusGoods);
        }
}

function delGoods() {
    //удаляем товар из корзины
    var id = $(this).attr('data-id');
    delete cart[id];
    saveCart();
    showCart();
}
function plusGoods() {
    //добавляет товар в корзине
    var id = $(this).attr('data-id');
    cart[id]++;
    saveCart();
    showCart();
}
function minusGoods() {
    //уменьшаем товар в корзине
    var id = $(this).attr('data-id');
    if (cart[id]==1) {
        delete cart[id];
    }
    else {
        cart[id]--;
    }
    saveCart();
    showCart();
}

function saveCart() {
    //сохраняю корзину в localStorage
    sessionStorage.setItem('cart', JSON.stringify(cart)); //корзину в строку
}

function isEmpty(object) {
    //проверка корзины на пустоту
    for (var key in object)
    if (object.hasOwnProperty(key)) return true;
    return false;
}
/*

function sendAll() {
    // src="../static/image_product/${item["image"][id]}">`;
    console.log("SEND");
    $.post( "../app/route.py" );
    if (isEmpty(cart)) {
        console.log("test_post")
           var send= $.post(
                "../app/route.py",


 */
function testorder(id) {
    id=cart;
    console.log(id);
    return id

}
function sendAll() {
    sessionStorage.removeItem(cart);
if (isEmpty(cart)) {
    console.log("test_post")
            $.post('/cart', {
                cart: cart
             }),onResponse()//
            //function(data){
            //  console.log('test_data');
            //
            //  console.log(dat);
//
            //};
       //  // );
    }
    else {
        alert('Корзина пуста');
    }

}
 function onResponse(data){
                    console.log("Sesion")
                    sessionStorage.clear();
                    window.open("https://shop-4641.herokuapp.com/order", "_self");
                }

$(document).ready(function () {
   loadCart();
   $('.send-all').on('click', sendAll); // отправить письмо с заказом
});