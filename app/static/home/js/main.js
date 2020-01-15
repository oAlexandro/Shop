
var cart={};//Корзина
var item={'id_product': [1, 2, 3, 4, 5, 6, 7, 8, 9],'name_of_product': ['Горшок из бетона', 'Горшок из бетона', 'Горшок из бетона', 'Горшок из бетона', 'Горшок из бетона', 'Свеча из бетона', 'Свеча из бетона', 'Свеча из бетона', 'Свеча из бетона'], 'price': [150, 120, 1500, 2000, 1200, 500, 700, 600, 550]}

var items1={};//Корзина
function box1(id) {
        console.log("TEXT")
        id=id-1;
     if(cart[id]==undefined)
    {
        cart[id]=1;
    }
    else {
        cart[id]++;
    }

    //console.log(cart);
    showMiniCart();
    saveCart();

}
function item2(id) {
        console.log("TEST INPUT")
     if(items1[id]==undefined)
    {
        items1[id]=1;
    }


   // localStorage.setItem('items1', JSON.stringify(items1)); //корзину в строку
   // localStorage.setItem('item', JSON.stringify(id));
  // saveCart();
    console.log("TEST INPUT")
    window.open("http://127.0.0.1:5000/cart", "_self");
    location.href = meni_1;
    $('.cart').html(out);
    

}
function showMiniCart() {

   // console.log(item["name_of_product"][1]);
    //показываю мини корзину
           var out = '';
           for (var id in cart) {
               console.log("for");
                out += ` ${item["name_of_product"][id] }`;
                out += `  <button data-id="${id}" class="minus-good">-</button>  `;
                out += ` ${cart[id]}`;
                out += `  <button data-id="${id}" class="plus-good">+</button>  `;
                out += cart[id]*item["price"][id];
                out += '<br>';
           }
           $('.mini-cart').html(out);
           $('.plus-good').on('click', plusGood);
           $('.minus-good').on('click', minusGood);
           }
  //  for (var key in cart) {
  //      out += key +' --- '+ cart[key]+'<br>';
  //  }



function plusGood() {
    //добавляет товар в корзине
    var id = $(this).attr('data-id');
    cart[id]++;
    saveCart();
    showMiniCart();
}
function minusGood() {
    //уменьшаем товар в корзине
    var id = $(this).attr('data-id');
    if (cart[id]==1) {
        delete cart[id];
    }
    else {
        cart[id]--;
    }
    saveCart();
    showMiniCart();
}


function saveCart() {
    //сохраняю корзину в localStorage
    sessionStorage.setItem('cart', JSON.stringify(cart)); //корзину в строку
    //localStorage.setItem('item', JSON.stringify(items)); //корзину в строку

    //localStorage.setItem('item', JSON.stringify(cart)); //корзину в строку
}

function loadCart() {
    //проверяю есть ли в localStorage запись cart
    if (sessionStorage.getItem('cart')) {
        // если есть - расширфровываю и записываю в переменную cart
        cart = JSON.parse(sessionStorage.getItem('cart'));
        showMiniCart();

    }
}



$(document).ready(function () {
    loadCart();
});

//$(window).unload(function(){
// sessionStorage.removeItem(cart);
//});