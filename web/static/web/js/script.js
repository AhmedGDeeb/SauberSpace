$(document).ready(function () {
    // Fetch Available Times on Button Click
    $('#fetchTimes').click(function (event) {
        event.preventDefault(); // Prevent the default form submission or page refresh

        const selectedDate = $('#date').val();

        if (!selectedDate) {
            alert('Please select a date!');
            return;
        }

        console.log(selectedDate);
        
        // Simulate API Call for Available Times
        $.ajax({
            url: '/api/get_times', // Replace with your actual API endpoint
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ date: selectedDate }),
            success: function (response) {
                // Assume 'response' contains a list of available times
                const availableTimes = response.allowed_times; // Example: ["08:00", "09:00", ..., "14:00"]
                console.log(availableTimes);

                // Select the container
                const timesContainer = document.getElementById("timesContainer");

                // Clear any existing content in the container
                timesContainer.innerHTML = "";

                // Create a button group with radios
                if (response.allowed_times.length==0) {
                    alert("No available Times at this date.");
                }

                response.allowed_times.forEach((time, index) => {
                    // Create an input element of type checkbox
                    const radioInput = document.createElement("input");
                    radioInput.type = "radio";
                    radioInput.name = "hour";
                    radioInput.id = `hour${index}`;
                    radioInput.value = time;
                    radioInput.classList.add("btn-check");
                    radioInput.autocomplete="off";
                    radioInput.required = true;


                    // Create the label element styled as a button
                    const radioLabel = document.createElement("label");
                    radioLabel.htmlFor = `hour${index}`;
                    radioLabel.classList.add("btn", "btn-info");
                    radioLabel.textContent = time;

                    // Append the checkbox input and label to the container
                    timesContainer.appendChild(radioInput);
                    timesContainer.appendChild(radioLabel);
                    }
                )},
            error: function () {
                alert('Failed to fetch available times. Please try again.');
            }
        });
    });
});


$(document).ready(function () {
    // Fetch Available Times on Button Click
    $('#reserve').click(function (event) {
        event.preventDefault(); // Prevent the default form submission or page refresh

        const name = $('input[name="name"]').val();
        const phone = $('input[name="phone"]').val();
        const email = $('input[name="email"]').val();
        const message = $('textarea[name="message"]').val();
        const date = $('input[name="date"]').val();
        const hour = $('input[name="hour"]:checked').val();
        if (!name) {
            alert('Bitte geben Sie einen Namen ein!');
            return;
            }
            if (!phone) {
            alert('Bitte geben Sie eine Telefonnummer ein!');
            return;
            }
            if (!email) {
            alert('Bitte wählen Sie eine E-Mail-Adresse aus!');
            return;
            }
            if (!message) {
            alert('Bitte wählen Sie eine Nachricht aus!');
            return;
            }
            if (!date) {
            alert('Bitte wählen Sie ein Datum aus!');
            return;
            }
            if (!hour) {
            alert('Bitte wählen Sie eine Stunde aus!');
            return;
        }
        
        // Simulate API Call for Available Times
        $.ajax({
            url: '/api/reserve', // Replace with your actual API endpoint
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({name: name, phone:phone, email:email, message: message, date: date, hour: hour}),
            success: function (response) {
                alert('Erfolgreich reserviert.')
            },
            error: function () {
            alert('Verfügbare Zeiten konnten nicht abgerufen werden. Bitte versuchen Sie es erneut.');
            }
        });
    });
});