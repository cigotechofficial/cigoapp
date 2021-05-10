function play(){
            var audio = new Audio(
			'https://media.geeksforgeeks.org/wp-content/uploads/20190531135120/beep.mp3');
            audio.play();
        }

// function showNotification(){
//     const notification = new Notification("New Order",{
//         body: "Hey You Got A New Order"
//     });
// }
// 
// function notification(){
//     if (Notification.permission === "granted"){
//         showNotification();
//     }
//     else if(Notification.permission !== "denied"){
//         Notification.requestPermission().then(permission => {
//             if (permission === "granted"){
//                 showNotification();
//             }
//         });
//     }
// }




var previousorderlen = 1;
var currentorderlen;


// function updatePrevOrderLen(newlen){
// 	previousorderlen = newlen;
// }


var req = new XMLHttpRequest();
var url = 'getNewDeliveryOrder';

function drawTable(table_name, data) {
	if (table_name == 'neworder') {
		tableid = 'neworderdelivery'
		check_status = 0
		tablecolour = 'dark'
		modaltarget = 'seeordermodal'
		addressmodaltarget = 'viewaddmodel1'
		modalcontentid = 'modalcontent'
		addressmodalcontentid = 'addressmodalcontent1'
		orderid = 'neworderid'
		table_name = neworder
	} else if (table_name == 'delivering') {
		tableid = 'delivering'
		check_status = 1
		tablecolour = 'secondary'
		modaltarget = 'seeordermodaldelivering'
		addressmodaltarget = 'viewaddmodel2'
		modalcontentid = 'modalcontentdelivering'
		addressmodalcontentid = 'addressmodalcontent2'
		orderid = 'deliveringorderid'
		table_name = delivering
	} else {
		tableid = 'done'
		check_status = 2
	}
	var div = document.getElementById(tableid);
	div.innerHTML = "";
	var table = document.createElement('TABLE');

	var row = table.insertRow(0);

	row.className = 'bg-gradient-' + tablecolour + ' text-white'

	var sno = row.insertCell(0);
	var table_no = row.insertCell(1);
	var seebutton_header = row.insertCell(2);
	var address_header = row.insertCell(3);
	var delete_header = row.insertCell(4);

	sno.innerHTML = "Sno";
	table_no.innerHTML = "Phone No.";
	seebutton_header.innerHTML = "Orders";
	address_header.innerHTML = "Address";
	delete_header.innerHTML = "Delete";

	var s = 0
	for (var i = 0; i < data.length; i++) {
		if (data[i].status == check_status) {

			s = s + 1
			var row_entry = table.insertRow(table.rows.length);
			row_entry.id = data[i].order_id.toString();

			var sno_entry = row_entry.insertCell(0);
			var table_no_entry = row_entry.insertCell(1);
			var seebutton_entry = row_entry.insertCell(2);
			var address_entry = row_entry.insertCell(3);
			var deleteorder = row_entry.insertCell(4);

			var iddel = data[i].order_id.toString();

			sno_entry.innerHTML = s;
			table_no_entry.innerHTML = data[i].phone;
			seebutton_entry.innerHTML = '<button type="button" data-toggle="modal" data-target="#' + modaltarget + '" id="' + i + '"class="seebutton_' + tableid + ' btn btn-outline-secondary btn-sm ">View</button>';
			address_entry.innerHTML = '<button type="button" data-toggle="modal" data-target="#' + addressmodaltarget + '" id="' + i + '"class="viewaddressbutton_' + tableid + ' btn btn-outline-secondary btn-sm ">View</button>';
			deleteorder.innerHTML = '<button type="button"  id="' + iddel + '"class="deletedelivery_' + tableid + ' btn btn-outline-danger btn-sm ">Delete</button>';
			


		}
	}
	table.className = 'table text-center table-hover table-light'
	div.appendChild(table);

	if (tableid == 'neworderdelivery'){
		var currentorderlen = table.rows.length
		// console.log(previousorderlen , currentorderlen)

		if (currentorderlen > previousorderlen) {

			// alert("You have new orders!");
			swal("You have a new order!")
			// notification();
			// showNotification();
			play();
		}
		previousorderlen = currentorderlen;
	}


	// updatePrevOrderLen(currentorderlen);

}



function seeFunction(modalcontentid, data, orderid, buttonid) {
	var idstr = buttonid;

	var itemsObj = JSON.parse(data[idstr].items_json);
	var orderString = '';

	for (x in itemsObj) {
		orderString += itemsObj[x].toString();
		orderString = orderString.split('₹')[0]
		orderString = orderString.replace(",", " - ");
		orderString = orderString.replace(",", " - ");
		orderString = orderString.slice(0, -2);
		orderString += '<br>';

	}
	// console.log("Getting ", modalcontentid, orderidhiddendiv, orderid);
	modaldiv = document.getElementById(modalcontentid);
	modaldiv.innerHTML = orderString;

}

function viewAddressFunction(addressmodalcontentid, data, orderid, buttonid) {
	var idstr = buttonid;

	modaldiv = document.getElementById(addressmodalcontentid);
	modaldiv.innerHTML = data[idstr].address;
	// console.log(addressmodalcontentid)

}

function shiftFunction(shifturl, buttonid) {
	// console.log(buttonid)
	var id = buttonid;
	var url = ''+ shifturl +'?id=' + id;
	var req = new XMLHttpRequest();
	req.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {

			refreshorder();
		}
	};

	req.open("GET", url, true);
	req.send();


}

function refreshorder(){
req.onreadystatechange = function() {
	if (this.readyState === 4 && this.status === 200) {

		var data = JSON.parse(req.responseText);
		drawTable('delivering', data)
		drawTable('neworder', data)

		$('.seebutton_neworderdelivery').on('click', function() {
			seeFunction('modalcontent', data, 'neworderid', this.id);
		});		
		$('.viewaddressbutton_neworderdelivery').on('click', function() {
			viewAddressFunction('addressmodalcontent1', data, 'neworderid', this.id);
		});
		$('.deletedelivery_neworderdelivery').on('click', function() {
			shiftFunction('shifttodelivery', this.id);
		});



		$('.seebutton_delivering').on('click', function() {
			seeFunction('modalcontentdelivering', data, 'deliveringorderid', this.id);
		});		

		$('.viewaddressbutton_delivering').on('click', function() {
			viewAddressFunction('addressmodalcontent2', data, 'deliveringorderid', this.id);
		});		

		$('.deletedelivery_delivering').on('click', function() {
			shiftFunction('deletedelivery', this.id);
		});

		// $('.seebutton_acads').on('click', seeFunction.bind(this));

	}
};
req.open("GET", url, true);
req.send();
  setTimeout(refreshorder, 5000);
}
refreshorder();
