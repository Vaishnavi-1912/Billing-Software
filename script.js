// script.js

function calculateTotal() {
    let items = document.getElementsByName('item');
    let total = 0;
    for (let i = 0; i < items.length; i++) {
        if (items[i].checked) {
            total += parseFloat(items[i].getAttribute('data-price'));
        }
    }
    document.getElementById('total').innerText = 'Total: $' + total.toFixed(2);
}

}