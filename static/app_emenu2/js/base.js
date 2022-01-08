// --------------------------------------Call Waiter -------------------------------------------------------------------------
  var tableno = "{{tableno}}";
  function Waiterfun(){
   
          swal("Wait For A While, Waiter is coming!", {
            
          })
          .then((value) => {
          });

          var url = '../callwaiter?tableNo='+tableno;
          var req = new XMLHttpRequest();
            req.onreadystatechange = function(){
              if(this.readyState == 4 && this.status == 200){
                
              }
            };
            req.open("GET",url, true);
            req.send();
        
  }