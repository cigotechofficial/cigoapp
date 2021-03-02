			// --------------------------------------------------This is Manager Dashboard---------------------------------
			window.onload = function(){
				document.getElementById("orderstatusdiv").style.display = "none";
			}

			function btnorderstatus() {
				var x = document.getElementById("orderstatusdiv")
				if (x.style.display === "none") {
					x.style.display = "flex";
				} else {
					x.style.display = "none";
				}
			}


			// --------------------------------------------------Display waiter call----------------------------------------------------------
			var newLenwaiter = 0;
			var oldLenwaiter = 1;

			function refreshdisplaywaiter() {
				var url = 'getWaiterCall';
				var req = new XMLHttpRequest();
				req.onreadystatechange = function() {
					if (this.readyState == 4 && this.status == 200) {
						var data = JSON.parse(req.responseText);

						var div = document.getElementById('waiterid');

						div.innerHTML = "";
						var table = document.createElement('TABLE');

						var row = table.insertRow(0);
						row.className = 'bg-gradient-primary text-white'
						var table_no_w = row.insertCell(0);
						var clicktodelete = row.insertCell(1);

						table_no_w.innerHTML = "Table No.";
						clicktodelete.innerHTML = "Click To Delete";

						for (var i = 0; i < data.length; i++) {

							var row = table.insertRow(i + 1);
							var table_no_w = row.insertCell(0);
							var deleteorder = row.insertCell(1);

							table_no_w.innerHTML = data[i].table_no_w;
							deleteorder.innerHTML = '<button class="btn btn-info cart">Done</button>'
							deleteorder.id = data[i].id;
							deleteorder.onclick = function() {
								var id = this.id;
								var url = 'deletewaiter?id=' + id;
								var req = new XMLHttpRequest();
								req.onreadystatechange = function() {
									if (this.readyState === 4 && this.status === 200) {
										refreshdisplaywaiter();

									}
								};

								req.open("GET", url, true);
								req.send();


							}

						}
						table.className = 'table text-center table-hover '
						div.appendChild(table);
						// console.log(oldLenwaiter, newLenwaiter)
						newLenwaiter = table.rows.length
						if (newLenwaiter > oldLenwaiter) {
							// alert("You have new orders!");
							swal("You have a new waiter request!")
							oldLenwaiter = newLenwaiter;
							// play();
						}


					}
				};
				req.open("GET", url, true);
				req.send();
				setTimeout(refreshdisplaywaiter, 5000);
			}
			refreshdisplaywaiter();


			// ------------------------------------------------------Session Details Start-----------------------------------------------------

			function refreshsessiondetails() {
				var req = new XMLHttpRequest();
				// var url = 'getAllOrder';  
				var url = 'sessionDetailsManager';  
				req.onreadystatechange = function() {
					if (this.readyState === 4 && this.status === 200) {
						var data = JSON.parse(req.responseText);

						// console.log(data[3][data[3].length-1].table_no);

						// newLen = data.length;
						// if (newLen > oldLen){
						//     //alert("You have new orders!");
						//                   oldLen = newLen;
						//               }

						var div = document.getElementById('tabletextid');
						div.innerHTML = "";
						var table = document.createElement('TABLE');

						var row = table.insertRow(0);
						row.className = 'bg-gradient-dark text-white'
						var items_json = row.insertCell(0);
						var price_item = row.insertCell(1);
						var price_subtotal = row.insertCell(2);
						var price_total = row.insertCell(3);
						var table_no = row.insertCell(4);
						var clicktodelete = row.insertCell(5);

						items_json.innerHTML = "Items";
						table_no.innerHTML = "Table No.";
						price_item.innerHTML = "Item Price";
						price_subtotal.innerHTML = "Subtotal";
						price_total.innerHTML = "Total";
						status.innerHTML = "Status";
						clicktodelete.innerHTML = "Click To Delete";

						table_order = [];

						for (var i = 0; i < data.length; i++) {

							// if (data[i].status===2){
							//  continue;
							// }
							var row_entry = table.insertRow(table.rows.length);
							var items_json_entry = row_entry.insertCell(0);
							var price_item_entry = row_entry.insertCell(1);
							var price_subtotal_entry = row_entry.insertCell(2);
							var price_total_entry = row_entry.insertCell(3);
							var table_no_entry = row_entry.insertCell(4);
							var deleteorder = row_entry.insertCell(5);

							// Give unique id to each row's status cell
							// status_entry.id = "status_"+data[i].order_id.toString();
							var table_no = data[i][data[i].length - 1].table_no;
							row_entry.id = table_no.toString();

							var table_order_string = '';
							var table_prices_string = '';
							var table_subtotals_string = '';
							var table_total = 0;
							for (var entry = 0; entry < data[i].length - 1; entry++) {
								order = data[i][entry].items_json;
								order_prices = data[i][entry].prices;
								// console.log(order_prices;
								// pricesJson = JSON.parse(order_prices);
								// console.log(pricesJson);
								var item_price_str = '';
								var item_total_str = '';

								// console.log(order_price);
								orderJsonObj = JSON.parse(order);
								var orderString = '';

								for (x in orderJsonObj) {
									orderString += orderJsonObj[x].toString();
									orderString = orderString.replace(",", " - ");
									orderString += '<br>';
									// console.log(order_prices[x])
									item_price_str += order_prices[x][0].toString();
									item_total_str += order_prices[x][1].toString();
									item_price_str += '<br>';
									item_total_str += '<br>';
									table_total += order_prices[x][1];
								}
								table_order_string += orderString;
								table_prices_string += item_price_str;
								table_subtotals_string += item_total_str;
							}
							// console.log(table_no)
							// console.log(table_order_string);
							// var itemsObj = JSON.parse(data[i]);


							// items_json_entry.innerHTML = orderString;
							// table_no_entry.innerHTML = data[i].table_no;
							items_json_entry.innerHTML = table_order_string;
							table_no_entry.innerHTML = table_no;
							price_item_entry.innerHTML = table_prices_string;
							price_subtotal_entry.innerHTML = table_subtotals_string;
							price_total_entry.innerHTML = table_total.toString();
							deleteorder.innerHTML = '<button " class="btn btn-success cart">End Session</button>'
							deleteorder.order_id = table_no;

							deleteorder.onclick = function() {
								var id = this.order_id;
								var url = 'deleteorder?id=' + id;
								var req = new XMLHttpRequest();
								req.onreadystatechange = function() {
									if (this.readyState === 4 && this.status === 200) {
										refreshsessiondetails();

									}
								};

								req.open("GET", url, true);
								req.send();


							}

							// Status cell has checkbox
							// var checkbox = document.createElement('input');
							//                  checkbox.type = "checkbox";
							//                  checkbox.checked = data[i].status; // if status==1, then checkbox is checked
							//                  checkbox.onclick = function(){
							//                      saveStatus(this.parentNode.id); // On checkbox click, call saveStatus with the id as argument (id is "status_<order_id>")
							//                  };

							//                  status_entry.appendChild(checkbox)

						}
						table.className = 'table text-center table-hover'
						div.appendChild(table);


					}
				};
				req.open("GET", url, true);
				req.send();
				setTimeout(refreshsessiondetails, 5000);
			}
			refreshsessiondetails();

			// ------------------------------------------------------Session Details End-----------------------------------------------------




			// ------------------------------------------------New Order Table Start--------------------------------------------------------------
			var newLen = 0;
			var oldLen = 1;

			function refreshneworder() {
				var req = new XMLHttpRequest();
				var url = 'getNewOrderManager';
				req.onreadystatechange = function() {
					if (this.readyState === 4 && this.status === 200) {

						var data = JSON.parse(req.responseText);

						var div = document.getElementById('neworder');
						div.innerHTML = "";
						var table = document.createElement('TABLE');

						var row = table.insertRow(0);
						row.className = 'bg-gradient-dark text-white'
						var items_json = row.insertCell(0);
						var table_no = row.insertCell(1);
						var status = row.insertCell(2);

						items_json.innerHTML = "Items";
						table_no.innerHTML = "Table No.";
						status.innerHTML = "Shift to Cooking";

						table_order = [];

						for (var i = 0; i < data.length; i++) {
							if (data[i].status === 1 || data[i].status === 2) {
								continue;
							}

							var row_entry = table.insertRow(table.rows.length);
							var items_json_entry = row_entry.insertCell(0);
							var table_no_entry = row_entry.insertCell(1);
							var status_entry = row_entry.insertCell(2);




							var itemsObj = JSON.parse(data[i].items_json);
							var orderString = '';

							for (x in itemsObj) {
								orderString += itemsObj[x].toString();
								orderString = orderString.replace(",", " - ");
								orderString += '<br>';

							}

							items_json_entry.innerHTML = orderString;
							table_no_entry.innerHTML = data[i].table_no;
							status_entry.innerHTML = '<button  class="btn btn-info ">Shift to Cooking</button>';
							status_entry.id = data[i].order_id;

							status_entry.onclick = function() {
								var id = this.id;
								var url = 'shifttocookingmanager?id=' + id;
								var req = new XMLHttpRequest();
								req.onreadystatechange = function() {
									if (this.readyState === 4 && this.status === 200) {

										refreshneworder();
										refreshcooking();
									}
								};

								req.open("GET", url, true);
								req.send();



							}

						}
						table.className = 'table text-center table-hover'
						div.appendChild(table);

						newLen = table.rows.length

						// if (newLen > oldLen) {
						//     console.log(oldLen, newLen)
						//     // alert("You have new orders!");
						//     swal("You have a new order request!")
						//     oldLen = newLen;
						//     play();
						// }




					}
				};
				req.open("GET", url, true);
				req.send();

				setTimeout(refreshneworder, 5000);
			}
			refreshneworder();
			// ------------------------------------------------New Order Table End--------------------------------------------------------------
			// ------------------------------------------------Cooking Table Start--------------------------------------------------------------
			var newLen = 0;
			var oldLen = 1;

			function refreshcooking() {
				var req = new XMLHttpRequest();
				var url = 'getNewOrderManager';
				req.onreadystatechange = function() {
					if (this.readyState === 4 && this.status === 200) {

						var data = JSON.parse(req.responseText);

						var div = document.getElementById('cookingtable');
						div.innerHTML = "";
						var table = document.createElement('TABLE');

						var row = table.insertRow(0);
						row.className = 'bg-gradient-dark text-white'
						var items_json = row.insertCell(0);
						var table_no = row.insertCell(1);
						var status = row.insertCell(2);

						items_json.innerHTML = "Items";
						table_no.innerHTML = "Table No.";
						status.innerHTML = "Shift to Served";

						table_order = [];

						for (var i = 0; i < data.length; i++) {
							if (data[i].status === 2 || data[i].status === 0) {
								continue;
							}

							var row_entry = table.insertRow(table.rows.length);
							var items_json_entry = row_entry.insertCell(0);
							var table_no_entry = row_entry.insertCell(1);
							var status_entry = row_entry.insertCell(2);




							var itemsObj = JSON.parse(data[i].items_json);
							var orderString = '';

							for (x in itemsObj) {
								orderString += itemsObj[x].toString();
								orderString = orderString.replace(",", " - ");
								orderString += '<br>';

							}

							items_json_entry.innerHTML = orderString;
							table_no_entry.innerHTML = data[i].table_no;
							status_entry.innerHTML = '<button  class="btn btn-info ">Served</button>';
							status_entry.id = data[i].order_id;

							status_entry.onclick = function() {
								var id = this.id;
								var url = 'shifttoservedmanager?id=' + id;
								var req = new XMLHttpRequest();
								req.onreadystatechange = function() {
									if (this.readyState === 4 && this.status === 200) {

										refreshcooking();
									}
								};

								req.open("GET", url, true);
								req.send();



							}

						}
						table.className = 'table text-center table-hover'
						div.appendChild(table);

						newLen = table.rows.length

						// if (newLen > oldLen) {
						//     console.log(oldLen, newLen)
						//     // alert("You have new orders!");
						//     swal("You have a new order request!")
						//     oldLen = newLen;
						//     play();
						// }




					}
				};
				req.open("GET", url, true);
				req.send();

				setTimeout(refreshcooking, 5000);
			}
			refreshcooking();
			// ------------------------------------------------Cooking Table End--------------------------------------------------------------

			// ------------------------------------------------Verify Payment Start--------------------------------------------------------------

			var newLen = 0;
			var oldLen = 1;

			function refreshverifypaymenttable() {
				var req = new XMLHttpRequest();
				var url = 'verifypaymenttable';
				req.onreadystatechange = function() {
					if (this.readyState === 4 && this.status === 200) {

						var data = JSON.parse(req.responseText);

						var div = document.getElementById('verifypaymenttable');
						div.innerHTML = "";
						var table = document.createElement('TABLE');

						var row = table.insertRow(0);
						row.className = 'bg-gradient-primary text-white'
						var timeendsession = row.insertCell(0);
						var totalamount = row.insertCell(1);
						// var method = row.insertCell(2);
						var verified = row.insertCell(2);

						timeendsession.innerHTML = "Time Of End Session";
						totalamount.innerHTML = "Total Payment";
						// method.innerHTML = "Payment Method";
						verified.innerHTML = "Payment Verified";

						table_order = [];

						for (var i = 0; i < data.length; i++) {
							if (data[i].status === 1) {
								continue;
							}
							var row_entry = table.insertRow(table.rows.length);
							var timeendsession_entry = row_entry.insertCell(0);
							var totalamount_entry = row_entry.insertCell(1);
							// var method_entry = row_entry.insertCell(2);
							var verified_entry = row_entry.insertCell(2);

							var dt = new Date(data[i].timestamp);
							const options = { year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', timeZone: 'UTC' };


							timeendsession_entry.innerHTML = dt.toLocaleString('en-IN', options);
							totalamount_entry.innerHTML = data[i].totalamount;
							// method_entry.innerHTML = data[i].order_id;
							verified_entry.innerHTML = '<button  class="btn btn-info ">Payment Verified</button>';
							verified_entry.id = data[i].order_id;

							verified_entry.onclick = function() {
								var id = this.id;
								var url = 'shifttoverified?id=' + id;
								var req = new XMLHttpRequest();
								req.onreadystatechange = function() {
									if (this.readyState === 4 && this.status === 200) {

										refreshverifypaymenttable();
									}
								};

								req.open("GET", url, true);
								req.send();



							}

						}
						table.className = 'table text-center table-hover'
						div.appendChild(table);

						newLen = table.rows.length

						// if (newLen > oldLen) {
						//     console.log(oldLen, newLen)
						//     // alert("You have new orders!");
						//     swal("You have a new order request!")
						//     oldLen = newLen;
						//     play();
						// }




					}
				};
				req.open("GET", url, true);
				req.send();

				setTimeout(refreshverifypaymenttable, 5000);
			}
			refreshverifypaymenttable();

			// ------------------------------------------------Verify Payment End--------------------------------------------------------------

			// ------------------------------------------------------Hide/Show Start----------------------------------------------------------

			// ------------------------------------------------------Hide/Show Start----------------------------------------------------------