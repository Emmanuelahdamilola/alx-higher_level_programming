    // jQuery script
    $(document).ready(function () {
        // Add item to the list
        $("#add_item").on("click", function () {
            // Create a new list item
            var newItem = $("<li>Item</li>");
            // Append it to the UL with class "my_list"
            $(".my_list").append(newItem);
        });

        // Remove the last item from the list
        $("#remove_item").on("click", function () {
            // Select the last list item and remove it
            $(".my_list li:last-child").remove();
        });

        // Clear all items from the list
        $("#clear_list").on("click", function () {
            // Remove all list items
            $(".my_list").empty();
        });
    });
