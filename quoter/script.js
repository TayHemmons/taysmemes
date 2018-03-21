function quoteTest(product, baseprice)
{
    console.log('rfq: ' + product)
    if (isNaN(baseprice)){
        console.log('alert: invalid quote ' + baseprice + ' for: '+ product);
        document.getElementById("qproduct").innerHTML = product;
        document.getElementById("quote").innerHTML = 'ERROR';
        document.getElementById("buy").disabled = true;
        document.getElementById("sell").disabled = true;
    } else {
        var volatility = parseFloat(Math.random().toFixed(2))
        if (Math.random() >= 0.5){
            var price2 = baseprice + volatility
            } else {
                var price2 = baseprice - volatility
                }
        document.getElementById("qproduct").innerHTML = product 
        document.getElementById("quote").innerHTML = price2
        document.getElementById("buy").disabled = false;
        document.getElementById("sell").disabled = false;
    }
}
function dropQuote()
{
    document.getElementById("qproduct").innerHTML = ' '
    document.getElementById("quote").innerHTML = ' '
    console.log('dropped quote')
}
function positionAdd() {
    console.log('updating positions')
    var table = document.getElementById("positions");
    var row = table.insertRow(1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    cell1.innerHTML = 'Buy';
    cell2.innerHTML = document.getElementById("qproduct").innerHTML;
    cell3.innerHTML = document.getElementById("quote").innerHTML;
}