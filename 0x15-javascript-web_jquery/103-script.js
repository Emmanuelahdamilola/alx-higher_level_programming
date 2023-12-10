// jQuery script
    $(document).ready(function () {
        // Event handler for button click
        $("#btn_translate").on("click", function () {
            // Get the language code entered by the user
            var languageCode = $("#language_code").val();

            // Make a GET request to the translation API
            $.get("https://www.fourtonfish.com/hellosalut/hello/", { lang: languageCode }, function (data) {
                // Display the translation in the 'hello' div
                $("#hello").text(data.hello);
            });
        });
    });
