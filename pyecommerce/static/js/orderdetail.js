var ProductMessage = document.getElementById("product-message");
var ServiceMessage = document.getElementById("service_message");
var ServiceSendBtn = document.getElementById("btn-service-send");
var ProductSendBtn = document.getElementById("btn-product-send");

ServiceSendBtn.addEventListener("click", function(){
    var message = ServiceMessage.value;
    if(message !== ""){
        var orderid = this.dataset.orderid
        sendMessage(message,orderid);
    }else{
        window.alert("Vui lòng nhập phản hồi trước khi gửi!");
    }
});

ProductSendBtn.addEventListener("click", function(){
    var message = ProductMessage.value;
    if(message !== ""){
        var orderid = this.dataset.orderid
        sendMessage(message,orderid);
    }else{
        window.alert("Vui lòng nhập phản hồi trước khi gửi!");
    }
});


function sendMessage(message, orderid){
    var url = "/send_report/";
    fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({ message: message, orderid: orderid}),
      })
        .then((response) => {
          console.log(response);
          return response.json();
        })
        .then((data) => {
          console.log("data:", data);
          window.alert("Chúng tôi sẽ phản hồi bạn sớm nhất. Xin cảm ơn");
          location.reload();
        })
        .catch((error) => {
          location.reload();
          console.log("error: " + error);
        });
}