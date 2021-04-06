var emailinput = document.getElementById('emailinput');

var phoneinput = document.getElementById('phoneinput');

var addressinput = document.getElementById('addressinput');

var savebtn = document.getElementById("savebtn");



function setReadonly(idelement){
    var inputelement = document.getElementById(idelement);
    if(inputelement.readOnly){
        inputelement.readOnly = false;
    }
    else{
        inputelement.readOnly = true;
    }
}

emailinput.addEventListener('change', function(){
    savebtn.disabled = false;
});

phoneinput.addEventListener('change', function(){
    savebtn.disabled = false;
});
addressinput.addEventListener('change', function(){
    savebtn.disabled = false;
});
 function updateCustomerInf(phone, email, address){
     var emailinputvalue = emailinput.value;
     var phoneinputvalue = phoneinput.value;
     var addressinputvalue = addressinput.value;
    if(email !== emailinputvalue){
        let action = "updateEM"; 
        updateInf(emailinputvalue, action);
    }
    else{
        console.log("Email is not changed")
    }
    if(phone !== phoneinputvalue){
        let action = "updatePh";
        updateInf(phoneinputvalue, action);
    }
    else{
        console.log("Phone is not changed");
    }
    if(address !== addressinputvalue){
        let action = "updateAdd";
        updateInf(addressinputvalue, action);
    }
    else{
        console.log("Address is not changed");
    }
 }
 function updateInf(inputvalue, action){
    var url = "/update_customer_inf/";

    fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({ changedvalue: inputvalue, action: action}),
      })
        .then((response) => {
          console.log(response);
          return response.json();
        })
        .then((data) => {
          console.log("data:", data);
          location.reload();
        })
        .catch((error) => {
          location.reload();
          console.log("error: " + error);
        });
 }