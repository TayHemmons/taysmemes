function quoteTest(product, baseprice)
{
    console.log('rfq: ' + product)
    if (isNaN(baseprice)){
        console.log('alert: invalid quote ' + baseprice + ' for: '+ product);
        document.getElementById("quote").innerHTML = product + ' - ' + baseprice;
        document.getElementById("buy").disabled = true;
        document.getElementById("sell").disabled = true;
    } else {
        var volatility = parseFloat(Math.random().toFixed(2))
        if (Math.random() >= 0.5){
            var price2 = baseprice + volatility
            } else {
                var price2 = baseprice - volatility
                }
        document.getElementById("quote").innerHTML = product + ' - ' + price2;
        document.getElementById("buy").disabled = false;
        document.getElementById("sell").disabled = false;
    }
}
function dropQuote()
{
    document.getElementById("quote").innerHTML = 'No Active Quote'
    console.log('dropped quote')
}