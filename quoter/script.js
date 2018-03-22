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
        var volatility = parseFloat(Math.random())
        if (Math.random() >= 0.5){
            var price2 = baseprice + volatility
            } else {
                var price2 = baseprice - volatility
                }
        document.getElementById("qproduct").innerHTML = product 
        document.getElementById("quote").innerHTML = price2.toFixed(2)
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
function order(side) {
    var orderprice = document.getElementById("quote").innerHTML
    if (orderprice > 0){
        console.log('updating positions')
        var table = document.getElementById("positions");
        var row = table.insertRow(1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        var cell5 = row.insertCell(4);
        cell1.innerHTML = side;
        cell2.innerHTML = document.getElementById("qproduct").innerHTML;
        cell3.innerHTML = orderprice;
        dropQuote()
        //using 100 quantity until we put in a quantity feature
        cell4.innerHTML = 100
        //javascript sucks
        cell5.innerHTML = (100 * orderprice).toFixed(2)
    }
}

