// add to cart on store component
var updateBtns = document.getElementsByClassName('update-cart');

for (i = 0; i< updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, "Action:", action)

        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log('User is not authenticated')
        }else{
            updateUserOrder(productId, action)
        }
    })
}
// request to server
function updateUserOrder(productId, action){
    console.log('User is authenticated, sending data ...')
    var url = '/update_item/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action': action})
    })
    .then((response) =>{
        console.log(response);
        return response.json();
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload();
    })
    .catch((error) => {
        location.reload();
        console.log('error: ' + error)
    });
}

//change in cart component
var onchangeQuantity = document.getElementsByName('onchangeQuantity');

for (i = 0; i< onchangeQuantity.length; i++){
    onchangeQuantity[i].addEventListener('change', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        var quantityValue = this.value;
        console.log('productId:', productId, "Action:", action, "quantityValue", quantityValue);
        console.log('USER:', user);
        if(user == 'AnonymousUser'){
            console.log('User is not authenticated')
        }else{
            updateQuantityItem(productId, action, quantityValue)
        }
    })
}
// request to server
function updateQuantityItem(productId, action, quantity){
    console.log('User is authenticated, sending data ...');
    var url = '/update_item/';

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action': action, 'quantity': quantity})
    })
    .then((response) =>{
        console.log(response.body);
        return response.json();
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload();
    })
    .catch((error) => {
        location.reload();
        console.log('error: ' + error)
    });
}
// on delete order-item
var ondeleteOrderItem = document.getElementsByName('ondeleteOrderItem');
// request to server
for (i = 0; i< ondeleteOrderItem.length; i++){
    ondeleteOrderItem[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, "Action:", action,)

        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log('User is not authenticated')
        }else{
            deleteOrderItem(productId, action)
        }
    })
}
function deleteOrderItem(productId, action){
    console.log('User is authenticated, sending data ...')
    var url = '/update_item/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action': action})
    })
    .then((response) =>{
        console.log(response);
        return response.json();
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload();
    })
    .catch((error) => {
        location.reload();
        console.log('error: ' + error)
    });
}

// update size option
var checkedSmall = document.getElementById('Small')
console.log(checkedSmall);

for (i = 0; i< checkedSmall.length; i++){
    checkedSmall[i].addEventListener('checked', function(){
        if(checkedSmall[i].checked){
            console.log(checkedSmall[i].value);
        }else{
            console.log("uncheck");
        }
    });
}
