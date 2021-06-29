//https://api.thedogapi.com/v1

function get_breeds(url) {
    var uri = url + '/breeds'
    $.get(uri, function(response){
        $.each(response, function(index, element) {
            $("#perros").append("<option value='" + element.name + "'>" + element.name + "</option>");
        });
    });
}

function get_breeds_by_name(url, name) {
    var uri = url + '/images/search?q=' + name;
    $.get(uri, function(response){
        $.each(response, function(index, element) {
            $("#dog_image").empty();
            $("#dog_image").append("<img id=\"imagen-"+element.id+"\" src=\""+element.url+"\" class=\"img-thumbnail\" style=\"width:400px;height:300px;\" />");
        });
    });
}