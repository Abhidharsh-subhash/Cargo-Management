function job(x){
    var name = /^[A-Za-z ]+$/;

    if (x.comments.value == "") {
        alert('Please enter your comments');
        x.comments.focus();
        return false;
    }
    else if (!x.comments.value.match(name)) {
        alert('Your comments contain invalid characters');
        x.comments.focus();
        return false;
    }
}