$(document).ready(function(){
    $("#checkboxShowPassword").change(function(){
        if (this.checked)
        {
            $("#inputPassword").get(0).type = "text";
        }
        else
        {
            $("#inputPassword").get(0).type = "password";
        }
    });
});