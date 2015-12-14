String.prototype.capitalize = function() {
        return this.charAt(0).toUpperCase() + this.slice(1);
};


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
    table.className = 'product-list sortable';
    var header = table.createTHead();
    var row = header.insertRow(0);
    row.insertCell(0).innerHTML = '<b>Dealer</b>';
    row.insertCell(1).innerHTML = '<b>Link</b>';
    row.insertCell(2).innerHTML = '<b>Image</b>';
    row.insertCell(3).innerHTML = '<b>Price</b>';

    for (var i=0; i < boxes.length; ++i) {
        if (boxes[i].checked) {
            var url = '/api/' + boxes[i].name;
            var request = new XMLHttpRequest();
            request.open('POST', url, false);
            request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
            request.send('query='+text);

            var data = JSON.parse(request.responseText);
            var tbody = document.createElement('tbody');
            for (var j=0; j < data.length; ++j) {
                if (data[j]['price'] === '')
                    continue;
                var rw = tbody.insertRow(-1);
                rw.insertCell(-1).innerHTML = boxes[i].name.capitalize();
                rw.insertCell(-1).innerHTML = '<a href="'+data[j]['url']+'">'+data[j]['title']+'</a>';
                rw.insertCell(-1).innerHTML = '<img src="'+data[j]['img']+'">';
                rw.insertCell(-1).innerHTML = data[j]['price'];
            }
            table.appendChild(tbody);
        }
    }

    sorttable.makeSortable(table);
    div = document.getElementsByClassName('products')[0];
    div.appendChild(table);

    return false;
}
