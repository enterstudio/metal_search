String.prototype.capitalize = function() {
        return this.charAt(0).toUpperCase() + this.slice(1);
}


function search() {
    var text_el = document.getElementsByName('query')[0];
    var text = text_el.value;
    if (text === '') {
        alert('You need to specify a search term');
        return false;
    }
    var boxes = document.getElementsByClassName('dealer');

    var div = document.getElementsByClassName('products')[0];
    if (div.childNodes)
        div.removeChild(div.childNodes[0]);
    var table = document.createElement('table');
    table.border = "1";
    table.className = 'product-list';
    var row = table.insertRow(0);
    row.insertCell(0).innerHTML = '<b>Dealer</b>';
    row.insertCell(1).innerHTML = '<b>Link</b>';
    row.insertCell(2).innerHTML = '<b>Image</b>';
    row.insertCell(3).innerHTML = '<b>Price</b>';

    for (var i=0; i < boxes.length; ++i) {
        if (boxes[i].checked) {
            var url = '/api/' + boxes[i].name;
            var request = new XMLHttpRequest();
            request.onreadystatechange = function() {
                console.log(request.responseURL);
                if (request.status >= 200 && request.status < 400) {
                    var data = JSON.parse(request.responseText);
                    for (var j=0; j < data.length; ++j) {
                        if (data[j]['price'] === '')
                            continue;
                        var row = table.insertRow(-1);
                        // row.insertCell(-1).innerHTML = boxes[i].name.capitalize();
                        row.insertCell(-1).innerHTML = request.responseURL.slice(request.responseURL.lastIndexOf('/')+1).capitalize();
                        row.insertCell(-1).innerHTML = '<a href="'+data[j]['url']+'">'+data[j]['title']+'</a>';
                        row.insertCell(-1).innerHTML = '<img src="'+data[j]['img']+'">';
                        row.insertCell(-1).innerHTML = data[j]['price'];
                    }
                }
                else {
                    // did not work
                }
            };
            request.open('POST', url, true);
            request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
            request.send('query='+text);
        }
    }

    var div = document.getElementsByClassName('products')[0];
    div.appendChild(table);

    return false;
}

