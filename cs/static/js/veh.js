function book(x){
    var name = /^[A-Za-z ]+$/;
    var num = /^[0-9]+$/;

    if (x.vehiclename.value == "") {
        alert('Please enter your vehiclename');
        x.vehiclename.focus();
        return false;
    }
    else if (!x.vehiclename.value.match(name)) {
        alert('Your vehiclename contain invalid characters');
        x.vehiclename.focus();
        return false;
    }
    if (x.registrationno.value == '') {
        alert('Please enter your registration number');
        x.registrationno.focus();
        return false;
    }
    else if (!x.registrationno.value.match(num)) {
        alert('Your registration number contains invalid characters');
        x.registrationno.focus();
        return false;
    }
    if (x.source.value == "") {
        alert('Please enter your source');
        x.source.focus();
        return false;
    }
    else if (!x.source.value.match(name)) {
        alert('Your source contain invalid characters');
        x.source.focus();
        return false;
    }
    if (x.destination.value == "") {
        alert('Please enter your destination');
        x.destination.focus();
        return false;
    }
    if (x.capacity.value == '') {
        alert('Please enter your capacity');
        x.capacity.focus();
        return false;
    }
}