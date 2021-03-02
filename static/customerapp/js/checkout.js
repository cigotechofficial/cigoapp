if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}
 
console.log(cart);
var sum = 0;
if ($.isEmptyObject(cart)) {
    //if object is empty
    mystr = `<p>Your cart is empty, please add some items to your cart before sending order!</p>`
    $('#items').append(mystr);
} 
else {
    for (item in cart) {
        var name = cart[item][1];
        var qty = cart[item][0];
        sum = sum + qty;
        mystr = `<li class="list-group-item d-flex justify-content-between align-items-center">
                            ${name}
                            <span class="badge badge-primary badge-pill">${qty}</span>
                        </li>`
        $('#items').append(mystr);
    }
}
$('#itemsJson').val(JSON.stringify(cart));

// {% if thank %}

// swal("Thanks For Ordering With Us!", {

//     })
//     .then((value) => {
//         localStorage.clear();
//         document.location.href = "/customerapp/menu";
//     });


// { % endif % }