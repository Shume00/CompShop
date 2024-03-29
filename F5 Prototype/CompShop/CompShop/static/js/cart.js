var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function (){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productID:', productId, 'action:', action)

        console.log('User:', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserCart(productId, action)
        }
    })
}

function updateUserCart(productId, action){
    console.log('User is logged in. Sending data...')

    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productID': productId, 'action': action})
    })
        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log('data', data)
            location.reload()
        })
}