function form(x){
    var name = /^[A-Za-z ]+$/;
	var phone = /^[0-9]+$/;
	var mailformat = /^[a-zA-Z0-9._]+$/;

    if (x.name.value == "") {
        alert('Please enter your name');
        x.name.focus();
        return false;
    }
    else if (!x.name.value.match(name)) {
        alert('Your name contain invalid characters');
        x.name.focus();
        return false;
    }
    if (x.address.value == "") {
        alert('Please enter your address');
        x.address.focus();
        return false;
    }
    if (x.gender.value == "") {
        alert('Please select your address');
        x.gender.focus();
        return false;
    }
    if (x.mobileno.value == '') {
        alert('Please enter your mobile number');
        x.mobileno.focus();
        return false;
    }
    else if (!x.mobileno.value.match(phone)) {
        alert('Your mobile number contains invalid characters');
        x.mobileno.focus();
        return false;
    }
    else if (x.mobileno.value.length != 10) {
        alert('Invalid mobile number');
        x.mobileno.focus();
        return false;
    }
    else {
        var a = x.mobileno.value.split("");
        if (a[0] != 9 && a[0] != 8 && a[0] != 7 && a[0] != 6) {
            alert('Invalid mobile number');
            x.mobileno.focus();
            return false;
        }
    }
    if (x.place.value == "") {
        alert('Please enter your place');
        x.place.focus();
        return false;
    }
    else if (!x.place.value.match(name)) {
        alert('Your place contain invalid characters');
        x.place.focus();
        return false;
    }
    if (x.email.value == '') {
        alert('Please enter your email');
        return false;
    }
    else{
        var mailid= x.email.value;
        var maillen = mailid.length;
        var atpos = mailid.indexOf('@');
        var dotpos = mailid.lastIndexOf('.');
        var domain = mailid.split('@');
        var domain2 = domain[0].split('');

        if(atpos<0 || atpos+2>dotpos || dotpos+2>maillen){
            alert("Invalid email id");
            return false;
        }
        if(!domain[0].match(mailformat)){
            alert("email contain invalid characters");
            return false;
        }
        if(!isNaN(domain2[0]) || domain2[0] == "_"){
            alert("email contain invalid characters");
            return false;
        }
    }
    if(x.password.value == ""){
        alert("please enter your new password");
        x.password.focus();
        return false;
    }
    if(x.repassword.value == ""){
        alert("please re-enter your new password");
        x.repassword.focus();
        return false;
    }
    if(x.password.value != x.repassword.value){
        alert("passwords are not matching");
        x.repassword.focus();
        return false;
    }
}