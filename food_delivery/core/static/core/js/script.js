'use-strict';

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

    const productName = document.querySelector('.sproduct__title');
    const productSold = document.getElementById('sproduct__sold');
    const productQuantity = document.getElementById('quantity');
    const productSuccess = document.querySelector('.product__success');

    data = {
        "productName": productName.innerText,
        "productSold": productSold.value,
        "productQuantity": productQuantity.value
    }
    fetch('/add-cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data)
    }).then(res => {
        return res.json()
    }).then(result => {
        console.log(result);

        if (!result['isLogged']) {
            window.location.href = '/login';
        }
        productSuccess.innerText = result['message'];
        productSuccess.style.top = '0';
        
        setTimeout(() => {
            productSuccess.style.top = '-3.4rem';
        }, 2000);

    })
}
// Ajax Calls
// Event listeners

const eventListeners = () => {
    const quantityIncrease = document.querySelector('.cart__increase');
    const quantityDecrease = document.querySelector('.cart__decrease');
    const productQuantity = document.getElementById('quantity');
    const addToCartBtn = document.getElementById('add-to-cart');
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
}
// Event listeners

eventListeners();
