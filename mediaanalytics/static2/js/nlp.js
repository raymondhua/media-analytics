function topWords(data, tableName) {
    var table = document.getElementById(tableName);
    for (var i = data.length; i > 0; i--) {
        var row = table.insertRow(0);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        cell1.innerHTML = i;
        cell2.innerHTML = data[i-1].word;
        cell3.innerHTML = data[i-1].frequently;
    }
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    cell1.innerHTML = "<b>Rank</b>";
    cell2.innerHTML = "<b>Word</b>";
    cell3.innerHTML = "<b>Frequency</b>";
}

function notMatch(data, tableName) {
    var table = document.getElementById(tableName);
    for (var i = data.length; i > 0; i--) {
        var row = table.insertRow(0);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        cell1.innerHTML = data[i-1].request;
        cell2.innerHTML = data[i-1].word;
    }
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell1.innerHTML = "<b>Words</b>";
    cell2.innerHTML = "<b>Odd one out</b>";
}

function similarity(data, tableName) {
    var table = document.getElementById(tableName);
    for (var i = data.length; i > 0; i--) {
        var row = table.insertRow(0);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        cell1.innerHTML = data[i-1].word1;
        cell2.innerHTML = data[i-1].word2;
        cell3.innerHTML = data[i-1].similarity;
    }
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    cell1.innerHTML = "<b>First word</b>";
    cell2.innerHTML = "<b>Second word</b>";
    cell3.innerHTML = "<b>Similarity %</b>";
}

function similarWords(data, tableName) {
    var table = document.getElementById(tableName);
    for (var i = data.length; i > 0; i--) {
        var row = table.insertRow(0);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        cell1.innerHTML = i;
        cell2.innerHTML = data[i-1].word;
        cell3.innerHTML = data[i-1].frequently;
    }
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    cell1.innerHTML = "<b>Rank</b>";
    cell2.innerHTML = "<b>Word</b>";
    cell3.innerHTML = "<b>Similarity %</b>";
}

function analogy(data, tableName) {
    var table = document.getElementById(tableName);
    for (var i = data.length; i > 0; i--) {
        var row = table.insertRow(0);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        cell1.innerHTML = data[i-1].x;
        cell2.innerHTML = data[i-1].y;
        cell3.innerHTML = data[i-1].z;
        cell4.innerHTML = data[i-1].word;
    }
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    cell1.innerHTML = "<b>X</b>";
    cell2.innerHTML = "<b>Y</b>";
    cell3.innerHTML = "<b>Z</b>";
    cell4.innerHTML = "<b>?</b>";
}

function specificWord(data, tableName) {
    var table = document.getElementById(tableName);
    for (var i = data.length; i > 0; i--) {
        var row = table.insertRow(0);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        cell1.innerHTML = data[i-1].word;
        cell2.innerHTML = data[i-1].rank;
        cell3.innerHTML = data[i-1].count;
        cell4.innerHTML = data[i-1].frequency;
    }
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    cell1.innerHTML = "<b>Word</b>";
    cell2.innerHTML = "<b>Rank</b>";
    cell3.innerHTML = "<b>Count</b>";
    cell4.innerHTML = "<b>Frequency</b>";
}

function loadTSNEImage(canvas, imageName, headerName, headerText) { 
    var ctx = canvas.getContext("2d");
    var img = new Image();
    img.onload = function() {
        canvas.height = canvas.width * (img.height / img.width);

        var oc = document.createElement('canvas'),
            octx = oc.getContext('2d');

        oc.width = img.width * 0.8;
        oc.height = img.height * 0.8;
        
        ctx.drawImage(img, -20, -20, oc.width, oc.height);

        document.getElementById(headerName).innerHTML = headerText;
    };
    img.src = imageName;
}