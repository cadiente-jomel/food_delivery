const quantityIncrease = document.querySelector('.cart__increase');
const quantityDecrease = document.querySelector('.cart__decrease');
const productQuantity = document.getElementById('quantity');
const addToCartBtn = document.getElementById('add-to-cart');



//CSRFToken
const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
// CSRFToken

// Ajax calls
const addToCart = () => {
    fetch('/add-cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({"name": "Jomel Cadiente"})
    }).then(res => {
        return res.json()
    }).then(result => {
        console.log(result)
    })
}
// Ajax Calls
// Event listeners
quantityIncrease.addEventListener('click', () => {
    let value = productQuantity.value;
    productQuantity.value = parseInt(value) + 1;
});
quantityDecrease.addEventListener('click', () => {
    let value = productQuantity.value;
    if (value > 1) {
        productQuantity.value = parseInt(value) - 1;
    }

    if (value < 2) {
        quantityDecrease.style.cursor = 'not-allowed';
    } else {
        quantityDecrease.style.cursor = 'pointer';
    }
});

quantityDecrease.addEventListener('mouseover', () => {
    let value = productQuantity.value;
    if (value < 2) {
        quantityDecrease.style.cursor = 'not-allowed';
    } else {
        quantityDecrease.style.cursor = 'pointer';
    }
});

addToCartBtn.addEventListener('click', addToCart);
// Event listeners


