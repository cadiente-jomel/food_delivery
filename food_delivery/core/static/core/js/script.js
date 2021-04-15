const quantityIncrease = document.querySelector('.cart__increase');
const quantityDecrease = document.querySelector('.cart__decrease');
const productQuantity = document.getElementById('quantity');

quantityIncrease.addEventListener('click', () => {
    let value = productQuantity.value;
    productQuantity.value = parseInt(value) + 1;
});
quantityDecrease.addEventListener('click', () => {
    let value = productQuantity.value;
    if (value > 1) {
        productQuantity.value = parseInt(value) - 1;
    }
});

