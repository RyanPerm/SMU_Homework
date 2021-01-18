var table_data = data; // from data.js

$(document).ready(function() {
    buildFilters();
    buildTable();

    //Event Listener
    $("#filter-btn").on("click", function(e) {
        e.preventDefault();
        buildTable();
    });
    $("#form").on("submit", function(e) {
        e.preventDefault();
        buildTable();
    });
});

function buildFilters() {
    var unq_countries = [...new Set(table_data.map(x => x.country))];
    unq_countries.forEach(function(val) {
        var newOption = `<option>${val.toUpperCase()}</option>`;
        $('#country').append(newOption);
    });

    var unq_states = [...new Set(table_data.map(x => x.state))];
    unq_states.forEach(function(val) {
        var newOption = `<option>${val.toUpperCase()}</option>`;
        $('#state').append(newOption);
    });

    var unq_shapes = [...new Set(table_data.map(x => x.shape))];
    unq_shapes.forEach(function(val) {
        var newOption = `<option>${val.toUpperCase()}</option>`;
        $('#shape').append(newOption);
    });
}

function buildTable() {
    var dateFilt = $("#datetime").val();
    var cityFilt = $("#city").val();
    var stateFilt = $("#state").val();
    var countryFilt = $("#country").val();
    var shapeFilt = $("#shape").val();

    // Apply filters
    var filteredData = table_data;
    if (dateFilt) {
        filteredData = filteredData.filter(row => row.datetime === dateFilt.toLowerCase());
    }
    if (cityFilt) {
        filteredData = filteredData.filter(row => row.city === cityFilt.toLowerCase());
    }
    if (stateFilt) {
        filteredData = filteredData.filter(row => row.state === stateFilt.toLowerCase());
    }
    if (countryFilt) {
        filteredData = filteredData.filter(row => row.country === countryFilt.toLowerCase());
    }
    if (shapeFilt) {
        filteredData = filteredData.filter(row => row.shape === shapeFilt.toLowerCase());
    }

    if (filteredData.length === 0) {
        alert("No Data Found!");
    }

    buildTableString(filteredData);
}

function buildTableString(data) {
    var tbody = $("#ufo-table>tbody");

    tbody.empty();

    //append data
    data.forEach(function(row) {
        var newRow = "<tr>"
            // loop through each Object (dictionary)
        Object.entries(row).forEach(function([key, value]) {
            // set the cell data
            newRow += `<td>${value}</td>`
        });

        //append to table
        newRow += "</tr>";
        tbody.append(newRow);
    });
}