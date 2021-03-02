

var req = new XMLHttpRequest();
var url = 'neworderwaiter';

function drawTable(table_name, data) {
	if (table_name == 'neworder') {
		tableid = 'neworderwaiter'
		check_status = 0
		tablecolour = 'danger'
		modaltarget = 'seeordermodal'
		modalcontentid = 'modalcontent'
		orderid = 'neworderid'
		orderidhiddendiv = 'orderidhidden1'
		table_name = neworder
	} else if (table_name == 'cooking') {
		tableid = 'cooking'
		check_status = 1
		tablecolour = 'primary'
		modaltarget = 'seeordermodalcooking'
		modalcontentid = 'modalcontentcooking'
		orderid = 'cookingorderid'
		orderidhiddendiv = 'orderidhidden2'
		table_name = cooking
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

	sno.innerHTML = "Sno";
	table_no.innerHTML = "Table";
	seebutton_header.innerHTML = "Orders";

	var s = 0
	for (var i = 0; i < data.length; i++) {
		if (data[i].status == check_status) {

			s = s + 1
			var row_entry = table.insertRow(table.rows.length);
			row_entry.id = data[i].order_id.toString();

			var sno_entry = row_entry.insertCell(0);
			var table_no_entry = row_entry.insertCell(1);
			var seebutton_entry = row_entry.insertCell(2);

			sno_entry.innerHTML = s;
			table_no_entry.innerHTML = data[i].table_no;
			seebutton_entry.innerHTML = '<button type="button" data-toggle="modal" data-target="#' + modaltarget + '" id="' + i + '"class="seebutton_' + tableid + ' btn btn-outline-secondary btn-sm ">See</button>';

		}
	}
	table.className = 'table text-center table-hover table-light'
	div.appendChild(table);

}



function seeFunction(modalcontentid, data, orderidhiddendiv, orderid, buttonid) {
	var idstr = buttonid

	var itemsObj = JSON.parse(data[idstr].items_json);
	var orderString = '';

	for (x in itemsObj) {
		orderString += itemsObj[x].toString();
		orderString = orderString.replace(",", " - ");
		orderString += '<br>';

	}
	console.log("Getting ", modalcontentid, orderidhiddendiv, orderid);
	modaldiv = document.getElementById(modalcontentid);
	modaldiv.innerHTML = orderString;

	orderidhidden = document.getElementById(orderidhiddendiv);
	orderidhidden.innerHTML = '<input type="hidden" name="' + orderid + '" value="' + data[idstr].order_id + '">';
}

function refreshorder(){
req.onreadystatechange = function() {
	if (this.readyState === 4 && this.status === 200) {

		var data = JSON.parse(req.responseText);
		drawTable('cooking', data)
		drawTable('neworder', data)

		$('.seebutton_neworderwaiter').on('click', function() {
			seeFunction('modalcontent', data, 'orderidhidden1', 'neworderid', this.id);
		});

		$('.seebutton_cooking').on('click', function() {
			seeFunction('modalcontentcooking', data, 'orderidhidden2', 'cookingorderid', this.id);
		});

		// $('.seebutton_acads').on('click', seeFunction.bind(this));

	}
};
req.open("GET", url, true);
req.send();
  setTimeout(refreshorder, 5000);
}
refreshorder();
// -----------------------------------------------------------waiter call start----------------------------------------------------------
function refreshwaitercall(){
var urlw = 'getWaiterCall';
var reqw = new XMLHttpRequest();
reqw.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
		var data = JSON.parse(reqw.responseText);

		var div = document.getElementById('waiterid');

		div.innerHTML = "";
		var table = document.createElement('TABLE');

		var row = table.insertRow(0);
		row.className = 'bg-gradient-dark text-white'
		var table_no_w = row.insertCell(0);
		var clicktodelete = row.insertCell(1);

		table_no_w.innerHTML = "Table No.";
		clicktodelete.innerHTML = "Click To Delete";

		for (var i = 0; i < data.length; i++) {

			var row = table.insertRow(i + 1);
			var table_no_w = row.insertCell(0);
			var deleteorder = row.insertCell(1);

			table_no_w.innerHTML = data[i].table_no_w;
			deleteorder.innerHTML = '<button " class="btn btn-info cart">Done</button>'
			deleteorder.id = data[i].id;
			deleteorder.onclick = function() {
				var id = this.id;
				var url = 'deletewaiter?id=' + id;
				var req = new XMLHttpRequest();
				req.onreadystatechange = function() {
					if (this.readyState === 4 && this.status === 200) {

						refreshwaitercall();
					}
				};

				req.open("GET", url, true);
				req.send();

				
			}

		}
		table.className = 'table text-center table-hover '
		div.appendChild(table);


	}
};
reqw.open("GET", urlw, true);
reqw.send();
  setTimeout(refreshwaitercall, 5000);
}
refreshwaitercall();
// -----------------------------------------------------------waiter call end----------------------------------------------------------

// --------------------------------------------------------------waiter endsession start---------------------------------------------


// --------------------------------------------------------------waiter endsession end---------------------------------------------