// Find out the cart items from localStorage

if (localStorage.getItem('cart') == null) {
    var cart = {};
    hidecheckoutnav();
}
else {
    cart = JSON.parse(localStorage.getItem('cart'));
    updateCart(cart);
    if (Object.keys(cart).length == 0){hidecheckoutnav();}
    else{showcheckoutnav();}
}

// Checkout Navbar Functions
function hidecheckoutnav(){
	let checkoutnav = document.getElementById('checkoutnav');
	checkoutnav.classList.add("hidden");
}
function showcheckoutnav(){
	let checkoutnav = document.getElementById('checkoutnav');
	checkoutnav.classList.remove("hidden");
}
// If the add to cart button is clicked, add/increment the item
//$('.cart').click(function() {
$('.divpr').on('click', 'button.cart', function() {
    var idstr = this.id.toString();
    if (cart[idstr] != undefined) {
        qty = cart[idstr][0] + 1;
    } else {
        qty = 1;
        name = document.getElementById('name' + idstr).innerHTML;
        price = document.getElementById('price' + idstr).innerHTML;
        cart[idstr] = [qty, name, price];
    }
    updateCart(cart);
});
// -----------------------------------------------------------------------------------------------------------
// Add Popover to cart
// $('#popcart').popover();
// updatePopover(cart);

// function updatePopover(cart) {
//     // console.log('We are inside updatePopover');
//     var popStr = "";
//     // popStr = popStr + "<h5> Table {{table_no}} Order List :  </h5><div class='mx-2 my-2'>";
//     popStr = popStr + "<h5> Order List :  </h5><div class='mx-2 my-2'>";
//     var i = 1;
//     for (var item in cart) {
//         popStr = popStr + "<b>" + i + "</b>. ";
//         popStr = popStr + document.getElementById('name' + item).innerHTML.slice(0, 14)+ "_____ Qty: " + cart[item][0] + "<br>";

//         i = i + 1;

//     }

//     // popStr = popStr + "<button class='btn btn-primary' onclick='clearCart()' id ='clearCart'>Clear Cart</button>"
//     popStr = popStr + "<button class='btn btn-primary' onclick='clearCart()' id ='clearCart'>Clear Cart</button>";
//     // alert(popStr);
//     console.log(popStr);
//     document.getElementById('popcart').setAttribute('data-content', popStr);
//     $('#popcart').popover('hide');

// }

// ------------------------------------
// Add Popover to cart
$('#popcart').popover();
updatePopover(cart);

function updatePopover(cart) {
    // console.log('We are inside updatePopover');
    var popStr = "";
    // popStr = popStr + "<h5> Table {{table_no}} Order List :  </h5><div class='mx-2 my-2'>";
    popStr = popStr + "<h5> Order List :  </h5><div class='mx-2 my-2'>";
    var i = 1;
    for (var item in cart) {
        popStr = popStr +  `<li class="list-group-item d-flex justify-content-between align-items-center">` +
                    document.getElementById('name' + item).innerHTML+ `<span class="badge badge-primary badge-pill">` + cart[item][0] + `</span>`;

        i = i + 1;

    }

    popStr = popStr + "<button class='btn btn-primary' onclick='clearCart()' id ='clearCart'>Clear Cart</button></div>"
    // alert(popStr);
    console.log(popStr);
    document.getElementById('popcart').setAttribute('data-content', popStr);
    $('#popcart').popover('hide');

}
// ----------------------------------------------------------------------------------------------------
function clearCart() {

    cart = JSON.parse(localStorage.getItem('cart'));
    for (var item in cart) {
        document.getElementById('div' + item).innerHTML = '<button id="' + item + '" class="btn btn-sm btn-primary cart">Add</button>'
    }
    localStorage.clear();
    cart = {};
    updateCart(cart);
}

function updateCart(cart) {
    var sum = 0;
    for (var item in cart) {
        sum = sum + cart[item][0];
        document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-sm btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item][0] + "</span> <button id='plus" + item + "' class='btn btn-sm btn-primary plus'> + </button>";
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = sum;
    showcheckoutnav();
    updatePopover(cart);
}
// If plus or minus button is clicked, change the cart as well as the display value
$('.divpr').on("click", "button.minus", function() {
    a = this.id.slice(7);
    cart['pr' + a][0] = cart['pr' + a][0] - 1;
    cart['pr' + a][0] = Math.max(0, cart['pr' + a][0]);
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    updateCart(cart);
    if(cart['pr' + a][0] == 0 ){
		cart = JSON.parse(localStorage.getItem('cart'));
		delete cart['pr' + a]
		localStorage.setItem('cart',JSON.stringify(cart));
		document.getElementById('divpr' + a).innerHTML = '<button id="' + 'pr'+ a + '" class="btn  btn-sm btn-primary cart">Add</button>'
		updatePopover(cart);
		
    }
    cart = JSON.parse(localStorage.getItem('cart'));

    if(Object.keys(cart).length == 0){
    	hidecheckoutnav();
    }
    
});
$('.divpr').on("click", "button.plus", function() {
    a = this.id.slice(6, );
    cart['pr' + a][0] = cart['pr' + a][0] + 1;
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    updateCart(cart);
});

// function individualremove(a){
//     cart = JSON.parse(localStorage.getItem('cart'));
//     for (var item in cart) {
    	
//         document.getElementById('div' + item).innerHTML = '<button id="' + item + '" class="btn btn-primary cart">Add</button>'
    
//     }
//     localStorage.clear();
//     cart = {};
//     updateCart(cart);
//     hidecheckoutnav();
// }
function deleteall(){
	localStorage.clear();
}

const getFontSize = (textLength) => {
  // const baseSize = 10
  const max_size = 3
  const min_size = 1.5
  const sensitivity = 10

  var fontSize 
  
  if (textLength >= max_size * sensitivity) {
    fontSize = min_size
  }
  else if (textLength < 6) {
    fontSize = max_size
  }
  else {
    fontSize = max_size - textLength/sensitivity
  }
  
  return `${fontSize}vh`
}

const boxes = document.querySelectorAll(".abc")
// console.log("Boxes length")
// console.log(boxes.length)
boxes.forEach(box => {
    console.log(getFontSize(box.textContent.length))
    box.style.fontSize = getFontSize(box.textContent.length)
    // box.style.fontSize = '9vw'
    // console.log(box.style)
})

