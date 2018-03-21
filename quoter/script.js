function quoteTest(product, price)
{
    document.getElementById("quote").innerHTML = product + ' - ' + price;
    console.log('rfq: ' + product)
    if (isNaN(price)){
        console.log('alert: invalid quote ' + price + ' for: '+ product)
        document.getElementById("buy").disabled = true;
        document.getElementById("sell").disabled = true;
    } else {
        document.getElementById("buy").disabled = false;
        document.getElementById("sell").disabled = false;
    }
}
function dropQuote()
{
    document.getElementById("quote").innerHTML = 'No Active Quote'
    console.log('dropped quote')
}