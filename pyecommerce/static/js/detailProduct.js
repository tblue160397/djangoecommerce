var updateBtns = document.getElementsByClassName('detail-product');

for (i = 0; i< updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, "Action:", action)

    })
}