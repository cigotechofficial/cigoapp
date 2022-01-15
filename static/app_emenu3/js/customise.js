function customiseFunc(btnid,customisablefields){
    var div = document.getElementById('customItemData');
    div.innerHTML = "";
    var table = document.createElement('TABLE');
    var row = table.insertRow(0);
    row.className = 'bg-success bg-gradient text-white';
    
    var select = row.insertCell(0);
    var price = row.insertCell(1);
    
    select.innerHTML = "Select";
    price.innerHTML = "Price";

  	for (var i = 0; i < customisablefields.length; i++) {
      if (btnid == customisablefields[i].product_id ){
        var row_entry = table.insertRow(table.rows.length);
        row_entry.id = customisablefields[i].product_id.toString();
  
        var select_entry = row_entry.insertCell(0);
        var price_entry = row_entry.insertCell(1);
  
        select_entry.innerHTML =  customisablefields[i].customitemname;
        price_entry.innerHTML = customisablefields[i].customitemprice;
      }
    }

    
    table.className = 'table text-center '
    div.appendChild(table);
  } 