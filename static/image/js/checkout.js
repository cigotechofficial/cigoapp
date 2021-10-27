
if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}

var sum = 0;
if ($.isEmptyObject(cart)) {
    //if object is empty
    mystr = `<p>Your cart is empty, please add some items to your cart before sending order!</p>`
    $('#items').append(mystr);
} else {

    mystr = `<table class="table-responsive  ">
                    <thead class="thead-dark table-light  ">
                        <tr >
                            <th scope="col">Item</th>
                            <th scope="col">Price</th>
                            <th scope="col">Qty</th>
                            <th scope="col">Total</th>
                        </tr>
                    </thead>
                    <tbody class="table-light">`
    var subtotal = 0;
    for (item in cart) {
        var price = cart[item][2];
        var name = cart[item][1];
        var qty = cart[item][0];
        var x = price.replace('₹', '');
        var prodtotal = qty * x;

        subtotal = subtotal + prodtotal
        var cgst = Math.round(cgstval*subtotal/100)
        var sgst = Math.round(sgstval*subtotal/100)
        var discount = Math.round(discountval*subtotal/100)
        var total = Math.round(subtotal + cgst + sgst - discount)
        sum = sum + qty;
        mystr = mystr + `
                        <tr>
                            <td>${name}</td>
                            <td>${price}</td>
                            <td>${qty}</td>
                            <td>₹${prodtotal}</td>
                        </tr>`
    }
    mystr = mystr + `</tbody>
                    <tfoot class="table-secondary">
                        <tr>
                            <td scope="row"></td>
                            <th>Subtotal: </th>
                            <td></td>
                            <td>₹${subtotal}</td>
                        </tr>                        
                        <tr>
                            <td scope="row"></td>
                            <th>CGST: </th>
                            <td>${cgstval}%</td>
                            <td>₹${cgst}</td>
                        </tr>
                        <tr>
                            <td scope="row"></td>
                            <th>SGST: </th>
                            <td>${sgstval}%</td>
                            <td>₹${sgst}</td>
                        </tr>
                        <tr>
                            <td scope="row"></td>
                            <th>Discount: </th>
                            <td>${discountval}%</td>
                            <td>-₹${discount}</td>
                        </tr>
                        <tr>
                            <td scope="row"></td>
                            <th>Total Amount: </th>
                            <td></td>
                            <td>₹${total}</td>
                        </tr>
                    </tfoot>
                </table>`
    $('#items').append(mystr);

}
$('#itemsJson').val(JSON.stringify(cart));

