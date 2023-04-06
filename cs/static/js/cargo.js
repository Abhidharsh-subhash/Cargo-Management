function valid(x){
    var num = /^[0-9]+$/;
    
    if (x.weight.value == "") {
        alert('Please enter your weight');
        x.weight.focus();
        return false;
    }
    if (x.price.value == "") {
        alert('Please enter your price');
        x.price.focus();
        return false;
    }
    else if (!x.price.value.match(num)) {
        alert('Your price contain invalid characters');
        x.price.focus();
        return false;
    }
    if (x.fromaddress.value == "") {
        alert('Please enter fromaddress');
        x.fromaddress.focus();
        return false;
    }
    if (x.toaddress.value == "") {
        alert('Please enter toaddress');
        x.toaddress.focus();
        return false;
    }
    if (x.landmark.value == "") {
        alert('Please enter landmark');
        x.landmark.focus();
        return false;
    }
}