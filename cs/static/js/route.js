function route(x){
    if(x.route.value == ''){
        alert("Please enter the route")
        x.route.focus()
        return false
    }
}