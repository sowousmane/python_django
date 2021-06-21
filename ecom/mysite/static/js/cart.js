var updateBtns = document.getElementsByClassName ('update-cart');

for (let i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener ('click', function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log ('produit:', productId, 'Action:', action);
    console.log ('utlisateru: ', user);
    if(user === 'AnonymousUser'){
        console.log('no logged')
    }else{
      updateUserOrder(productId, action)  
    }
  });
}

function updateUserOrder(productId, action){
  console.log('user is logged in,  sening data...')
    var url = '/update_item/'

    fetch(url, {
      method:'POST',
      headers:{
        'Content-Type':'application/json',
        'X-CSRFToken': csrftoken,
      },
      body:JSON.stringify({'productId':productId, 'action':action})

    }).then((response) => {
      return response.json();
    }).then((data) => {
      location.reload()
    });
}