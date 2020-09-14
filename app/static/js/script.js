$(document).ready(function() {

	$('.toast').toast('show')
	
})


$(document).ready(function(){
    $("#my-modal").on("show.bs.modal", function(event){
        // Get the button that triggered the modal
        var button = $(event.relatedTarget);

        // Extract value from the custom data-* attribute
        var url = button.data("url");
        $(this).find('#confirm-delete').attr('href', url)
    });
});